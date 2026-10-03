# 7. Transferir um estado

**Pergunta:** o que é transferido quando nada material viaja de um qubit para outro?

**Objetivo:** entender o papel do par de Bell, das medições e dos dois bits clássicos. Reserve 60–90 minutos.

Alice possui q0 no estado |ψ⟩=α|0⟩+β|1⟩ e q1; Bob possui q2. Primeiro, q1 e q2 formam um par de Bell. Alice aplica CNOT de q0 para q1 e H em q0, depois mede q0 e q1. Ela envia os resultados m0 e m1 a Bob. Bob usa esses bits para corrigir q2.

| m0 | m1 | Correção em q2 |
|---:|---:|---|
| 0 | 0 | Nenhuma |
| 0 | 1 | X |
| 1 | 0 | Z |
| 1 | 1 | X e depois Z |

Antes das correções, o estado de Bob é X^m1 Z^m0 |ψ⟩, até a convenção de fase global. Aplicar primeiro X quando necessário e depois Z desfaz essa transformação.

## Experimento completo

Execute `python3 -m curso.experimentos teletransporte`.

Usamos (|0⟩+i|1⟩)/√2: a fase complexa torna o teste mais informativo que testar apenas 0 ou 1. O programa mostra uma execução sorteada e, depois, os quatro ramos por pós-seleção. Cada ramo tem probabilidade 1/4 e fidelidade final aproximadamente 1.

A fidelidade mede a concordância de q2 com o estado de entrada. O cálculo ignora os qubits medidos e compara amplitudes, incluindo suas fases. Apenas um histograma 50%/50% não seria suficiente.

Leia `teleport()` e localize preparação, recurso entrelaçado, medição e correções. A inicialização de α e β é feita diretamente na memória para definir o estado de teste conhecido; o protocolo não precisa conhecer esses coeficientes para transferi-lo.

## Desafios

1. Teste α=1, β=0 e depois α=0, β=1.
2. Remova temporariamente as correções. Todos os quatro ramos ainda funcionam para a entrada com fase complexa?
3. Alice fica com uma cópia utilizável do estado original?

<details><summary>Soluções comentadas</summary>

1. Todos os ramos corrigidos têm fidelidade 1 para as duas entradas.
2. Não. Para a entrada escolhida, alguns ramos produzem outro estado; um único caso favorável não valida o protocolo.
3. Não. Suas medições consomem a preparação original; o protocolo não clona um estado desconhecido.

</details>

**Limite:** a simulação representa Alice e Bob na mesma memória clássica. Em dispositivos reais, os dois bits precisam de comunicação clássica; não há transmissão instantânea ou teletransporte de matéria.


---

[← Módulo anterior](06-grover.md) · [Índice](../README.md) · [Próximo módulo →](08-matematica-ao-silicio.md)
