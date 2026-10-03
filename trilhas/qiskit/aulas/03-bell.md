# 3. Dois qubits em um estado conjunto

**Pergunta:** onde ficam as correlações de dois qubits no vetor?

**Objetivo:** preparar Bell em Qiskit e acompanhar a convenção dos índices. Tempo sugerido: 45 minutos.

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

circuito = QuantumCircuit(2)
circuito.h(0)
circuito.cx(0, 1)
estado = Statevector.from_instruction(circuito)
print(estado.data)
```

A ordem das entradas é 00, 01, 10, 11. O resultado tem amplitudes 1/√2 na primeira e na última posição; as outras são zero. O nome `cx` corresponde à CNOT: controle primeiro, alvo depois.

**Experimente:** acrescente `circuito.cx(0, 1)` e `circuito.h(0)`. A inversão retorna a 00. Agora coloque `circuito.z(0)` antes dessas duas operações inversas: o resultado muda para 01, embora o histograma de Bell antes da inversão continuasse igual.

**Desafios:** troque os papéis de q0 e q1 em toda a preparação. Depois substitua a primeira H por X.

<details><summary>Soluções comentadas</summary>

H em q1 seguida de CX de q1 para q0 também prepara o mesmo Bell. X em q0 seguida de CX de q0 para q1 prepara 11, um estado separável. A presença de uma porta CX não garante entrelaçamento para toda entrada.

</details>

**Limite:** contagens iguais em 00 e 11, isoladamente, não distinguem Bell de uma mistura clássica. A inversão investiga coerência. O acesso às amplitudes é uma possibilidade do simulador, não a leitura completa de um único par físico.


## Executar o exemplo da aula

Na raiz do repositório, com o ambiente virtual ativado:

```bash
python -m trilhas.qiskit.experimentos bell
```

[← Anterior](02-hadamard.md) · [Índice](../README.md) · [Próxima →](04-comparacao.md)
