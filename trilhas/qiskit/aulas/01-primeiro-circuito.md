# 1. Seu primeiro circuito em Qiskit

**Pergunta:** como uma biblioteca transforma sua ideia em um circuito?

**Objetivo:** construir um circuito e distinguir sua descrição da execução. Tempo sugerido: 30–45 minutos. Faça a instalação descrita no índice antes de começar.

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

circuito = QuantumCircuit(1)
circuito.x(0)
estado = Statevector.from_instruction(circuito)
print(estado.probabilities_dict())
```

`QuantumCircuit(1)` cria a descrição de um circuito com um qubit. `x(0)` acrescenta uma operação. Nenhuma dessas duas linhas aciona uma máquina quântica. `Statevector.from_instruction` calcula localmente o estado resultante, partindo de |0⟩.

O resultado esperado é probabilidade 1 para `1`. Execute o comando desta aula e confira também as amplitudes e amostras.

**Experimente:** acrescente outra X. Antes de executar, escreva a previsão. Agora use dois qubits e aplique X apenas em q0. O resultado será `01`: q0 fica à direita, como no Pequibit.

**Desafio:** prepare `10` com duas linhas após os imports.

<details><summary>Solução comentada</summary>

Use `circuito = QuantumCircuit(2)` e `circuito.x(1)`. A posição 1 identifica o qubit da esquerda na escrita binária. O vetor inicial é |00⟩.

</details>

**Limite:** estamos simulando um estado ideal. Criar um circuito não equivale a executá-lo em uma QPU ou na FPGA.


## Executar o exemplo da aula

Na raiz do repositório, com o ambiente virtual ativado:

```bash
python -m trilhas.qiskit.experimentos primeiro
```

[← Índice](../README.md) · [Índice](../README.md) · [Próxima →](02-hadamard.md)
