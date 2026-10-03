# 5. Grover com portas de alto nível

**Pergunta:** duas descrições diferentes podem representar o mesmo algoritmo?

**Objetivo:** construir oráculo e difusor com Qiskit. Tempo sugerido: 60 minutos.

A função `grover()` desta trilha começa com H nos dois qubits e aplica `cz(0, 1)` para marcar 11. O difusor usa H nos dois qubits, X nos dois, CZ, X nos dois e H nos dois.

O Pequibit implementa essa transformação com outra decomposição e uma convenção de fase global diferente. A aula anterior verifica que o estado final é fisicamente equivalente.

Acompanhe o cálculo ideal: após a preparação, todas as amplitudes são 1/2. O oráculo troca o sinal da última. A média passa a 1/4. A reflexão em torno da média leva as três primeiras amplitudes a zero e a última a 1, até uma fase global da decomposição.

**Experimente:** copie a função para um arquivo de estudo e remova o oráculo. Confira que o difusor sozinho não identifica a resposta. Retorne ao original e marque 00, envolvendo somente o CZ do oráculo com X nos dois qubits.

**Desafio:** por que não devemos envolver também o difusor nessa alteração?

<details><summary>Solução comentada</summary>

A condição de solução está no oráculo. O difusor continua refletindo em torno da mesma superposição inicial. Alterar ambos sem derivar a transformação pode mudar o algoritmo e a resposta.

</details>

**Limite:** esta é uma demonstração com uma resposta explicitamente escolhida. Não demonstra ganho de tempo sobre uma busca clássica. O custo do oráculo, a preparação dos dados e a execução precisam entrar em uma comparação prática.


## Executar o exemplo da aula

Na raiz do repositório, com o ambiente virtual ativado:

```bash
python -m trilhas.qiskit.experimentos grover
```

[← Anterior](04-comparacao.md) · [Índice](../README.md) · [Próxima →](06-hardware.md)
