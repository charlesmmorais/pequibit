# 2. Seu primeiro qubit

**Pergunta:** ter 50% de chance de obter 0 descreve tudo sobre um qubit?

**Objetivo:** distinguir amplitude de probabilidade e preparar superposição. Reserve 45 minutos. Você usará quadrados e raízes, apresentados aqui.

Um estado puro de um qubit é escrito como |ψ⟩ = α|0⟩ + β|1⟩. α e β são amplitudes. A probabilidade de medir 0 é |α|²; a de medir 1 é |β|². Elas somam 1. Para amplitudes reais, isso significa elevar ao quadrado; para complexas, usaremos o módulo.

A porta Hadamard, H, transforma |0⟩ em (|0⟩ + |1⟩)/√2. Cada amplitude vale aproximadamente 0,7071. Seu quadrado é 0,5. Usar amplitudes 0,5 e 0,5 seria um erro: os quadrados somariam apenas 0,5.

## Experimento

Execute `python3 software/reference.py examples/01_hadamard.qtg`.

```text
INIT 1
H 0
```

Antes de executar, anote as duas probabilidades esperadas. Compare os valores calculados com as mil amostras. As probabilidades são 0,5; as contagens não precisam ser exatamente 500 e 500.

A semente fixa permite repetir a mesma simulação. Ela é uma ferramenta de depuração, não uma fonte de aleatoriedade quântica física.

## Desafios

1. Um estado tem amplitudes √3/2 e 1/2. Quais são as probabilidades?
2. Edite seu circuito para executar X antes de H. Compare amplitudes e probabilidades.
3. A listagem das amplitudes equivale a medir um qubit real e conhecer seu estado completo?

<details><summary>Soluções comentadas</summary>

1. 3/4 e 1/4, ou 75% e 25%.
2. H|1⟩ = (|0⟩ − |1⟩)/√2. A segunda amplitude muda de sinal; as probabilidades continuam 50%/50%.
3. Não. A listagem é acesso à memória de um simulador. Uma medição individual retorna um resultado, não todas as amplitudes.

</details>

## Limite da experiência

Um histograma 50%/50% também pode vir de uma moeda clássica. A próxima aula mostra uma transformação que depende da fase e da coerência, não apenas dessa distribuição.

**Antes de seguir:** calcule uma probabilidade a partir de uma amplitude e explique por que contagem não é amplitude.


---

[← Módulo anterior](01-bits-e-circuitos.md) · [Índice](../README.md) · [Próximo módulo →](03-fase-e-interferencia.md)
