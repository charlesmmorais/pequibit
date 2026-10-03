# 1. Antes do qubit

**Pergunta:** o que um programa precisa guardar para representar uma moeda virada para cima?

**Objetivo:** reconhecer um bit, acompanhar uma porta X e ler a convenção de bits do projeto. Reserve de 30 a 45 minutos; saber abrir um terminal é suficiente.

Um bit tem dois valores possíveis: 0 e 1. Um circuito descreve operações sobre uma entrada. Podemos começar com 0, inverter o valor e obter 1. Inverter outra vez retorna a 0. A porta quântica X reproduz essa troca nos estados |0⟩ e |1⟩, mas também age sobre superposições que estudaremos depois.

Os símbolos |0⟩ e |1⟩ são nomes de estados, não operadores especiais de Python. A escrita se chama notação ket. Você não precisa decorar a terminologia para acompanhar o experimento.

## Faça sua previsão

Crie `meu_circuito.qtg` na raiz do projeto:

```text
INIT 2
X 0
```

Execute `python3 software/reference.py meu_circuito.qtg`.

Você esperava 01 ou 10? No Pequibit, q0 fica à direita. A saída é |01⟩ com probabilidade 1. Essa convenção também determina os endereços de memória: 00, 01, 10, 11 correspondem a 0, 1, 2, 3.

O programa mostra uma amplitude e uma probabilidade. Por enquanto, observe que uma amplitude igual a 1 produz probabilidade 1. A relação geral aparece na próxima aula.

## Desafios

1. Troque `X 0` por `X 1`. Qual estado aparece?
2. Aplique X duas vezes no mesmo qubit. O que retorna?
3. Como preparar 11 a partir de 00?

<details><summary>Soluções comentadas</summary>

1. Aparece 10: mudamos o bit da esquerda, q1.
2. Voltamos a 00. X é sua própria inversa.
3. Aplique `X 0` e `X 1`, em qualquer ordem. Como atuam em qubits diferentes, essas operações comutam.

</details>

## O que você demonstrou

Você acompanhou uma transformação determinística entre estados da base computacional. Isso ainda não exige superposição ou entrelaçamento. A diferença quântica começa a aparecer quando amplitudes e fases passam a importar.

**Antes de seguir:** explique por que `X 0` prepara 01 neste projeto, e não 10.


---

[← Início do curso](../README.md) · [Índice](../README.md) · [Próximo módulo →](02-primeiro-qubit.md)
