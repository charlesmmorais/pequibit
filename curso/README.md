# Pequibit — Do primeiro qubit ao circuito

**Pequenos circuitos. Grandes descobertas.**

Você vai escrever circuitos, prever resultados e descobrir por que amplitudes, fases e medições importam. No caminho, abriremos o simulador para entender suas contas e preparar o terreno para um executor em FPGA.

## Para quem é

Pessoas curiosas sobre programação, eletrônica e computação quântica. Não exigimos física avançada. É útil conhecer variáveis e funções; o início usa arquivos de texto com uma instrução por linha. A matemática entra junto com a experiência que precisa dela.

Carga sugerida: 7–9 horas incluindo exercícios e projeto, no seu ritmo. É um curso introdutório de estudo livre, sem promessa de certificação profissional.

## Prepare o ambiente

Instale Python 3.10 ou superior. Baixe o repositório pelo botão Code → Download ZIP no GitHub e extraia, ou use:

```bash
git clone https://github.com/charlesmmorais/pequibit.git
cd pequibit
python3 --version
python3 software/reference.py examples/01_hadamard.qtg
python3 -m unittest discover -s tests -v
```

Todos os comandos do curso partem da raiz `pequibit`, que contém `software`, `curso` e `tests`. No Windows, substitua `python3` por `py -3` se necessário. Não há instalação por pip, conta em nuvem ou placa obrigatória.

## Percurso

| Módulo | Experiência | Resultado de aprendizagem |
|---|---|---|
| [1. Antes do qubit](modulos/01-bits-e-circuitos.md) | X | Ler estados e convenções de bits |
| [2. Seu primeiro qubit](modulos/02-primeiro-qubit.md) | Hadamard | Converter amplitudes em probabilidades |
| [3. A fase muda o caminho](modulos/03-fase-e-interferencia.md) | H–Z–H | Explicar interferência e fase relativa |
| [4. Qubits em conjunto](modulos/04-entrelacamento.md) | Bell e inversão | Distinguir Bell de uma mistura clássica |
| [5. Medir muda a experiência](modulos/05-medicao.md) | Medição repetida | Usar medição com colapso |
| [6. Programar para encontrar](modulos/06-grover.md) | Grover de dois qubits | Separar oráculo de difusor |
| [7. Transferir um estado](modulos/07-teletransporte.md) | Teletransporte | Verificar as quatro ramificações |
| [8. Da matemática ao silício](modulos/08-matematica-ao-silicio.md) | Quantização de H | Identificar limites da representação numérica |

## Como aproveitar cada aula

Leia a pergunta, escreva uma previsão e só então execute. Mude uma coisa de cada vez. Registre o que esperava, o que observou e como explicaria a diferença a outra pessoa. Abra as soluções depois de tentar os desafios.

O curso simula circuitos ideais em um computador clássico. Os módulos 1–7 funcionam em software; o módulo 8 oferece uma ponte prática para engenharia digital. Não há RTL ou execução física na FPGA nesta versão.

## Materiais de apoio

- [Glossário](glossario.md)
- [Projeto final e critérios](projeto-final.md)
- [Guia para quem ensina](guia-do-educador.md)
- [Dificuldades frequentes](duvidas.md)
- [Fontes científicas](referencias.md)

## Executar os novos experimentos

```bash
python3 -m curso.experimentos medicao
python3 -m curso.experimentos grover
python3 -m curso.experimentos teletransporte
python3 -m curso.experimentos ponto-fixo
```

A API Python oferece medição e pós-seleção. O formato QTG continua restrito a INIT e portas; não tente inserir MEASURE no arquivo de circuito.

## Continue com Qiskit

Depois dos fundamentos, explore a [trilha opcional de Qiskit](../trilhas/qiskit/README.md), com seis aulas e comparação entre os simuladores.
