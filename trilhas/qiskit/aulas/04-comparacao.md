# 4. Dois simuladores, uma previsão

**Pergunta:** como descobrir um erro que um histograma não mostra?

**Objetivo:** usar Qiskit como referência independente para as contas do Pequibit. Tempo sugerido: 45–60 minutos.

O comando desta aula executa os quatro exemplos originais e Grover nos dois motores. Cada circuito é construído separadamente: em QTG/Python no Pequibit e com `QuantumCircuit` no Qiskit. Não estamos comparando um simulador com uma cópia da própria saída.

Cada linha informa três resultados:

| Campo | Verificação |
|---|---|
| `equivalent` | Estados equivalentes, admitindo fase global |
| `probability_error` | Maior diferença absoluta entre probabilidades |
| `norm_error` | Maior desvio da norma ao quadrado em relação a 1 |

O limite usado é 10⁻¹² para estes circuitos pequenos em ponto flutuante. Esse limite não deve ser copiado para o futuro hardware de 16 bits.

**Experimente no Python:**

```python
from trilhas.qiskit.experimentos import compare_vectors
s = 2**-0.5
print(compare_vectors([s, s], [-s, -s]))
print(compare_vectors([s, s], [s, -s]))
```

**Desafio:** antecipe a equivalência e o erro de probabilidades nos dois casos.

<details><summary>Solução comentada</summary>

O primeiro caso é equivalente: −1 multiplica o vetor inteiro e representa uma fase global. O segundo não é equivalente: somente uma componente muda de sinal. Nos dois casos as probabilidades coincidem. Por isso precisamos verificar também o estado.

</details>

A suíte adicional compara portas em circuitos gerados com semente fixa, incluindo fases complexas e CNOT em sentidos diferentes. Testes independentes aumentam confiança; não são prova de ausência de erros para todos os circuitos.

**Limite:** a comparação atual cobre evolução unitária e Grover. Não inclui a medição intermediária nem o teletransporte do Pequibit. Também não existe um adaptador geral Qiskit→FPGA nesta entrega.


## Executar o exemplo da aula

Na raiz do repositório, com o ambiente virtual ativado:

```bash
python -m trilhas.qiskit.experimentos comparar
```

[← Anterior](03-bell.md) · [Índice](../README.md) · [Próxima →](05-grover.md)
