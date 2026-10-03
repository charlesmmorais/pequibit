# 2. Probabilidades e amostras

**Pergunta:** por que mil resultados não precisam se dividir em duas metades exatas?

**Objetivo:** usar Hadamard e ler o vetor de estado. Tempo sugerido: 45 minutos.

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

circuito = QuantumCircuit(1)
circuito.h(0)
estado = Statevector.from_instruction(circuito)
estado.seed(42)
print(estado.data)
print(estado.probabilities_dict())
print(estado.sample_counts(1000))
```

As amplitudes são aproximadamente 0,7071 e 0,7071. Cada módulo ao quadrado vale 0,5. `sample_counts` sorteia uma amostra dessa distribuição sem modificar o vetor armazenado. A semente torna a experiência reproduzível dentro do ambiente usado.

A visualização inicial é textual: vetor, dicionário de probabilidades e contagens. Ela funciona sem bibliotecas gráficas e pode ser lida por ferramentas de acessibilidade. Gráficos são uma extensão opcional, não um requisito.

**Experimente:** varie o número de amostras e a semente. Compare proporções observadas com probabilidades calculadas. Não espere as mesmas contagens do Pequibit: as bibliotecas podem usar geradores diferentes.

**Desafio:** acrescente Z depois de H e compare vetor e probabilidades. Depois acrescente mais uma H.

<details><summary>Solução comentada</summary>

Z troca o sinal da amplitude de |1⟩, mas preserva o histograma 50%/50%. A última H produz |1⟩ por interferência. O sinal relativo contém informação que o histograma inicial não revela.

</details>

**Limite:** uma medição dentro do circuito não é suportada por esta forma de evolução unitária via `from_instruction`. Não adicione `measure_all()` a estes exemplos para obter o vetor. Amostragem e medição intermediária são tarefas diferentes.


## Executar o exemplo da aula

Na raiz do repositório, com o ambiente virtual ativado:

```bash
python -m trilhas.qiskit.experimentos hadamard
```

[← Anterior](01-primeiro-circuito.md) · [Índice](../README.md) · [Próxima →](03-bell.md)
