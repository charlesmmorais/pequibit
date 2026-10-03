# 3. A fase muda o caminho

**Pergunta:** por que duas Hadamards devolvem um resultado certo?

**Objetivo:** acompanhar interferência e conhecer a unidade imaginária. Reserve 45–60 minutos.

H atua sobre um par de amplitudes a e b por a'=(a+b)/√2 e b'=(a−b)/√2. Depois da primeira H em |0⟩, temos a=b=1/√2. Na segunda, a'=(2/√2)/√2=1 e b'=0. O cancelamento explica o retorno a |0⟩.

Execute `python3 software/reference.py examples/02_interference.qtg`. Agora compare com `python3 software/reference.py examples/04_phase.qtg`: H–Z–H produz |1⟩. Z troca o sinal da amplitude de |1⟩. A última H converte essa diferença de fase em uma diferença de probabilidades.

## Um pequeno passo para os complexos

Escrevemos um número complexo como a+bi, com i²=−1. Seu módulo ao quadrado é a²+b². Em Python, a unidade imaginária é `1j`. Assim, 1/√2 e i/√2 têm o mesmo módulo ao quadrado: 1/2.

S multiplica a amplitude de |1⟩ por i; T multiplica por exp(iπ/4). Não alteram imediatamente as probabilidades nessa base, mas podem alterar interferências posteriores.

Crie um circuito `INIT 1`, `H 0`, `S 0`, uma instrução por linha. Observe a parte imaginária na saída.

## Desafios

1. Compare H–S–S–H com H–Z–H.
2. Compare H–T–T com H–S.
3. Se multiplicarmos todas as amplitudes por −1, as previsões físicas mudam?

<details><summary>Soluções comentadas</summary>

1. São equivalentes: i²=−1, portanto S²=Z.
2. T²=S, pois somamos duas fases de π/4.
3. Não. Isso é uma fase global. Uma mudança relativa, aplicada somente a uma parte do vetor, pode alterar interferências.

</details>

## Limites e cuidado

Não somamos probabilidades para calcular H: somamos amplitudes e depois calculamos módulos ao quadrado. A matemática prevê o comportamento ideal; erros de arredondamento do simulador não são ruído de um dispositivo quântico real.

**Antes de seguir:** explique o resultado de H–Z–H sem recorrer à ideia de “duas moedas”.


---

[← Módulo anterior](02-primeiro-qubit.md) · [Índice](../README.md) · [Próximo módulo →](04-entrelacamento.md)
