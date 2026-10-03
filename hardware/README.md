# Primeiro núcleo Pequibit em SystemVerilog

**Dois qubits simulados, quatro amplitudes complexas e operações que podemos acompanhar.**

O núcleo já possui RTL, modelo inteiro de referência, testbench e comparação automatizada. Ele representa estados quânticos numericamente em hardware clássico. A integração da Tang Nano 20K — clock, reset externo, UART, constraints e bitstream — ainda está pendente.

## O que já funciona em simulação

| Recurso | Implementação |
|---|---|
| Inicialização | Estado zero nos dois qubits, também após reset |
| Portas | H, X e Z em qualquer alvo; CNOT nos dois sentidos |
| Componentes complexos | Parte real e imaginária processadas separadamente |
| Inspeção | Leitura de uma das quatro amplitudes por endereço |
| Preparação de teste | LOAD de uma amplitude completa |
| Erros | Opcode inválido, controle igual ao alvo, overflow |

Não há medição, gerador aleatório, portas S/T, amostragem ou normalização automática no RTL. O modelo Python ideal possui mais recursos que este primeiro núcleo.

## Execute antes de ter a placa conectada

Na raiz do repositório, instale Icarus Verilog e Yosys. Em Debian/Ubuntu:

```bash
sudo apt-get update
sudo apt-get install iverilog yosys
python3 -m unittest discover -s tests -v
python3 -m hardware.tools.check_core
```

No Windows, uma opção é executar esses comandos no Ubuntu pelo WSL. Aqui o teste é de lógica digital e não depende de acesso USB à placa.

A saída esperada do comparador é `PASS: 812 comandos comparados bit a bit`. O script cria arquivos temporários e remove-os ao terminar. Não é necessário instalar Qiskit.

Para repetir a síntese genérica:

```bash
yosys -p 'read_verilog -sv hardware/rtl/q14_hadamard.sv hardware/rtl/pequibit_core.sv; synth -top pequibit_core; check -assert; stat'
```

Essa síntese não gera bitstream Gowin, não seleciona a Tang Nano e não estabelece frequência máxima. O número de células genéricas não é um número de LUTs da placa.

## Como representamos um número

Cada componente é um inteiro de 16 bits com sinal, dividido por 16384. A faixa é de −2 a 1,99993896484375. Uma amplitude tem duas componentes e ocupa 32 bits. As quatro amplitudes são registradores nesta versão, não BSRAM.

H utiliza a aproximação 11585/16384 para 1/√2. Primeiro somamos/subtraímos com 17 bits; depois multiplicamos em 32 bits. Arredondamos ao inteiro mais próximo; um empate afasta de zero. Por exemplo, +5792,5 vira +5793 e −5792,5 vira −5793.

Se qualquer componente do resultado não couber em 16 bits, o comando inteiro é rejeitado, `error` pulsa e o vetor anterior permanece intacto. Não há saturação ou wrap silencioso. O núcleo não verifica norma física: LOAD pode produzir vetores não normalizados para depuração e testes de fronteira.

## Interface do núcleo

| Sinal | Contrato |
|---|---|
| `clk` | Clock único fornecido pelo integrador |
| `rst` | Reset síncrono, ativo em 1; aborta comando e prepara o estado zero |
| `start` | Amostrado quando `busy=0` |
| `opcode` | Operação de 3 bits |
| `target`, `control` | Índices de 1 bit: q0 ou q1 |
| `load_addr`, `load_real`, `load_imag` | Operandos de LOAD |
| `busy` | Comando em execução |
| `done`, `error` | Pulsos de um ciclo; erro é válido junto de done |
| `read_addr` | Índice da amplitude: 00, 01, 10, 11 |
| `read_real`, `read_imag` | Leitura combinacional; consumir após done ou em repouso |

Mantenha os operandos estáveis no clock de aceite. Na borda N com `start=1` e `busy=0`, o núcleo guarda o comando e eleva busy. Na borda N+1, ele executa, baixa busy e pulsa done. O integrador deve remover start após o aceite; mantê-lo alto até outro ciclo ocioso pode iniciar novo comando. Durante busy, entradas concorrentes são ignoradas. O reset tem prioridade.

O clock de 100 MHz usado pelo testbench é apenas uma escala de simulação sem atrasos físicos. Não é uma frequência validada de operação do projeto.

## Instruções do núcleo

| Código | Nome | Operandos usados |
|---:|---|---|
| 0 | INIT | Nenhum; limpa as quatro amplitudes e prepara 00 |
| 1 | H | target |
| 2 | X | target |
| 3 | Z | target |
| 4 | CX | control e target diferentes |
| 5 | LOAD | Endereço e componentes de uma amplitude |
| 6, 7 | Inválidos | Erro, vetor preservado |

Esses códigos são a interface interna do núcleo. Não constituem ainda um protocolo serial ou um parser QTG em hardware.

## Nossa primeira experiência

Emita INIT, H com target=0 e CX com control=0/target=1, aguardando done entre operações. As leituras inteiras devem ser:

| Endereço | Real | Imaginária | Valor aproximado |
|---|---:|---:|---|
| 00 | 11585 | 0 | 0,7070922852 |
| 01 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 |
| 11 | 11585 | 0 | 0,7070922852 |

O desvio em relação a 1/√2 vem da quantização. Comparar RTL com o modelo inteiro exige igualdade bit a bit; comparar com a física ideal exige tolerância e análise da norma. Não confunda essas duas verificações.

## Arquivos

- [Modelo inteiro](../software/fixed_reference.py): contrato aritmético.
- [Butterfly Hadamard](rtl/q14_hadamard.sv): soma, diferença e arredondamento.
- [Núcleo](rtl/pequibit_core.sv): estado, portas, controle e erros.
- [Testbench](tb/core_tb.sv): reset, handshake, resultados e timeout.
- [Comparador](tools/check_core.py): gera circuitos e vetores de teste.
- [Evidências](validacao.md): ferramentas e limites do que foi medido.

## Próximo passo: a sua Tang Nano 20K

Precisamos conferir a revisão impressa na placa (foto da frente e do verso), o ambiente de desenvolvimento disponível e a pinagem oficial correspondente. Depois serão implementados o top da placa, sincronização do reset, transporte UART e constraints. Finalmente: síntese Gowin, place-and-route, timing, bitstream e teste físico de Bell.

Nenhum arquivo de pinagem ou bitstream deve ser inferido apenas pelo nome “Tang”. O núcleo pode ser estudado e simulado agora, sem gravar a placa.
