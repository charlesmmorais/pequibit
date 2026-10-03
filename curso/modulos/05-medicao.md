# 5. Medir muda a experiência

**Pergunta:** medir duas vezes é igual a preparar e medir duas vezes?

**Objetivo:** distinguir amostragem repetida, medição intermediária e pós-seleção. Reserve 45 minutos.

Execute `python3 -m curso.experimentos medicao` a partir da raiz.

O experimento prepara |+⟩, lista probabilidades, amostra mil preparações e faz duas medições no mesmo estado. Após a primeira medição, a segunda retorna o mesmo bit se nenhuma porta for aplicada entre elas.

## Três operações diferentes

| Operação Python | Significado |
|---|---|
| `state.sample(1000, 42)` | Amostra preparações idênticas sem alterar o vetor guardado |
| `state.measure(0, rng)` | Sorteia um resultado e colapsa o estado conjunto |
| `state.collapse(0, 1)` | Seleciona o ramo 1 para análise e retorna sua probabilidade |

A última operação é pós-seleção matemática: não representa poder escolher o resultado físico. Um ramo de probabilidade zero é rejeitado.

A medição do alvo q com resultado b mantém apenas amplitudes cujos índices têm aquele bit. Para normalizar, dividimos as amplitudes restantes por √p, onde p é a probabilidade desse ramo.

## Experimente no interpretador Python

```python
import random
from software.reference import run
state = run('INIT 2
H 0
CNOT 0 1')
rng = random.Random(42)
a = state.measure(0, rng)
b = state.measure(1, rng)
print(a, b)
```

O primeiro resultado pode variar entre preparações; o segundo concorda com ele. O colapso altera o vetor conjunto, inclusive suas correlações.

## Desafios

1. Prepare |0⟩ e tente `collapse(0, 1)`.
2. Prepare |+⟩ novamente antes de cada medição. A segunda ainda precisa concordar com a primeira?
3. Qual é o vetor depois de selecionar o ramo 0 do estado de Bell?

<details><summary>Soluções comentadas</summary>

1. O modelo rejeita a operação; o ramo tem probabilidade zero.
2. Não. São preparações independentes; cada uma tem probabilidades 50%/50%.
3. |00⟩, normalizado. O peso desse ramo antes da seleção era 1/2.

</details>

**Antes de seguir:** explique por que `sample` não pode substituir uma medição intermediária no teletransporte. As APIs acima são do modelo Python; a linguagem QTG ainda não tem instrução de medição.


---

[← Módulo anterior](04-entrelacamento.md) · [Índice](../README.md) · [Próximo módulo →](06-grover.md)
