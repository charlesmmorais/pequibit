# 4. Qubits em conjunto

**Pergunta:** dois bits que sempre concordam provam entrelaçamento?

**Objetivo:** preparar Bell e distinguir correlação de coerência. Reserve 45–60 minutos.

Dois qubits precisam de quatro amplitudes: uma para cada estado 00, 01, 10 e 11. Um estado entrelaçado não pode ser escrito como produto dos estados individuais dos qubits. É uma propriedade do estado conjunto.

## Construa Bell

Execute `python3 software/reference.py examples/03_bell.qtg`.

```text
INIT 2
H 0
CNOT 0 1
```

Após H, o estado é (|00⟩+|01⟩)/√2. A CNOT usa q0 como controle e q1 como alvo: a parcela 01 vira 11, e 00 fica igual. Obtemos (|00⟩+|11⟩)/√2.

As amostras têm bits iguais, mas essa observação isolada não basta: um sorteio clássico que emite 00 ou 11 também gera o mesmo histograma.

## A experiência da inversão

Acrescente ao circuito `CNOT 0 1` e depois `H 0`. Execute novamente. O estado puro de Bell volta a 00. Se tivéssemos uma mistura clássica de 00 e 11, a mesma inversão produziria metade 00 e metade 01. A coerência entre as parcelas faz diferença.

O modelo atual guarda estados puros. Uma mistura clássica pode ser estudada como uma coleção de execuções separadas, com seus pesos; não deve ser codificada como uma única superposição.

## Desafios

1. Substitua H 0 por X 0 antes da CNOT. Qual resultado aparece?
2. Depois de preparar Bell, aplique Z 0. O histograma muda? E o circuito inverso?

<details><summary>Soluções comentadas</summary>

1. O estado final é 11, determinístico; essa preparação não cria entrelaçamento.
2. O histograma continua 00/11. O estado vira (|00⟩−|11⟩)/√2; a inversão agora produz 01. O sinal relativo importa.

</details>

## O que isso não faz

A correlação não permite enviar mensagens instantâneas. Aqui tudo é calculado por um computador clássico; nenhum par fisicamente entrelaçado é criado na FPGA.

**Antes de seguir:** diferencie “bits iguais nas amostras” de “estado coerente de Bell”.


---

[← Módulo anterior](03-fase-e-interferencia.md) · [Índice](../README.md) · [Próximo módulo →](05-medicao.md)
