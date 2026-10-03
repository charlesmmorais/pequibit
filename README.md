# Pequibit

**Pequenos circuitos. Grandes descobertas.**

Um laboratório educativo de computação quântica em FPGA, pensado para a Tang Nano 20K.

Como duas operações tão pequenas podem produzir um estado tão interessante? No Pequibit, você começa com essa pergunta, acompanha as amplitudes e constrói o hardware que faz as contas. Uma experiência de cada vez.

O nome aproxima **pequeno** e **qubit**: aprender começando por circuitos que conseguimos acompanhar. É um nome de trabalho; esta versão não constitui verificação de marca ou reserva de nome no GitHub.

## Onde estamos

**Versão inicial: base educativa e modelo de referência em Python.** Os exemplos locais, os oito módulos do curso e os testes estão implementados. O núcleo em FPGA, a comunicação serial e o bitstream ainda serão desenvolvidos. Não há medição de desempenho nem validação física da placa nesta versão.

## Aprenda com o curso

**[Pequibit — Do primeiro qubit ao circuito](curso/README.md)**: oito módulos, experimentos executáveis, desafios com soluções e projeto final. Comece sem placa e avance até a introdução ao hardware.

```bash
python3 -m curso.experimentos grover
python3 -m curso.experimentos teletransporte
```

O curso inclui medição com colapso e teletransporte no modelo Python. A implementação dessas operações em FPGA continua planejada.

## Trilha opcional: Qiskit

**[Pequibit com Qiskit — Da descoberta à programação](trilhas/qiskit/README.md)**: seis aulas, instalação isolada, comparação independente de estados e introdução à transpilação. O curso básico continua sem dependências externas.

## O que estamos construindo

Um simulador clássico de circuitos quânticos, com um futuro executor em hardware reconfigurável. Ele guarda amplitudes complexas e aplica as mesmas transformações matemáticas usadas para descrever circuitos ideais.

A FPGA não contém qubits físicos. O entrelaçamento é representado numericamente; não existe comunicação instantânea, teletransporte de matéria ou promessa de vantagem quântica. Justamente por ser uma simulação, podemos inspecionar cada amplitude e aprender com ela.

## Comece sem comprar nada

Você precisa apenas de Python 3.10 ou superior. O modelo não usa bibliotecas externas. Execute os comandos a partir da pasta do projeto:

```bash
python3 software/reference.py examples/01_hadamard.qtg
python3 software/reference.py examples/02_interference.qtg
python3 software/reference.py examples/03_bell.qtg
python3 -m unittest discover -s tests -v
```

No Windows, use `py -3` caso `python3` não esteja disponível.

O primeiro experimento mostra probabilidades de 50% para 0 e 1. O segundo aplica Hadamard duas vezes e retorna a 0. O terceiro produz o estado de Bell, com probabilidades de 50% para 00 e 11. Esses são valores calculados; as contagens de amostragem flutuam.

## Uma primeira descoberta

```text
INIT 2
H 0
CNOT 0 1
```

Partimos de |00⟩, criamos uma superposição e correlacionamos os qubits. O resultado é (|00⟩ + |11⟩)/√2. A história completa está no [laboratório de Bell](docs/04-laboratorios.md).

## Seu caminho pelo projeto

| Etapa | Pergunta | Leitura |
|---|---|---|
| Entender | O que é uma amplitude? | [Fundamentos](docs/01-fundamentos.md) |
| Construir | Como representar isso na FPGA? | [Arquitetura](docs/02-arquitetura.md) |
| Programar | Que instruções vamos usar? | [Linguagem QTG](docs/03-instrucoes.md) |
| Experimentar | Como conferir o resultado? | [Laboratórios](docs/04-laboratorios.md) |
| Evoluir | O que implementar primeiro? | [Roadmap](docs/05-roadmap.md) |
| Conferir | Como saber se está correto? | [Validação](docs/06-validacao.md) |

## Organização

| Caminho | Responsabilidade |
|---|---|
| `software/reference.py` | Modelo matemático executável |
| `curso/` | Oito módulos e experimentos de medição, Grover, teletransporte e quantização |
| `examples/` | Circuitos pequenos em texto |
| `tests/` | Verificações de comportamento |
| `hardware/rtl/` | Futuro núcleo SystemVerilog |
| `hardware/boards/tang-nano-20k/` | Futura integração específica da placa |
| `docs/` | Ciência, decisões, aulas e critérios de aceitação |
| `.github/workflows/tests.yml` | Testes automáticos do modelo Python |

## Objetivo da primeira versão em hardware

Dois qubits, inicialização, H, X, Z, CNOT e leitura de amplitudes por serial. Depois: oito qubits, fase complexa, amostragem e medição com colapso. A capacidade final será publicada com evidências de síntese e teste, não deduzida apenas da memória disponível.

## Participe

Uma pergunta bem escrita também é uma contribuição. Você pode revisar uma explicação, reproduzir um experimento, melhorar um teste ou implementar um módulo. Veja [CONTRIBUTING.md](CONTRIBUTING.md).

Fontes e leituras: [referências](docs/07-referencias.md). Preparação da publicação e proposta de licenciamento: [publicação](docs/08-publicacao.md).

## Primeiro teste na IBM

[Guia: criar conta, entender o Open Plan e executar Bell](guias/ibm-quantum-primeiro-teste.md). Inclui ensaio local e envio explícito a uma QPU. Nenhuma execução física foi realizada pelo projeto durante a elaboração do guia.
