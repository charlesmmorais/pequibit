# 6. Programar para encontrar

**Pergunta:** como aumentar a chance de uma resposta sem simplesmente escrevê-la na saída?

**Objetivo:** separar oráculo, difusor e medição em Grover. Reserve 60 minutos.

Nosso universo contém quatro candidatos: 00, 01, 10 e 11. O oráculo é uma operação que reconhece a solução e inverte sua fase. Neste exemplo educativo, escolhemos 11 explicitamente. Isso serve para entender o mecanismo, não para alegar que descobrimos uma resposta desconhecida de forma útil.

Execute `python3 -m curso.experimentos grover`. O resultado ideal é probabilidade 1 em 11. Leia a função `grover()` em `curso/experimentos.py`: ela usa apenas portas já estudadas.

## Acompanhe as amplitudes

Duas Hadamards preparam [1/2,1/2,1/2,1/2]. O oráculo CZ muda o último sinal: [1/2,1/2,1/2,−1/2]. A média é 1/4.

O difusor padrão transforma cada amplitude a em 2×média−a. As três primeiras viram zero; a última vira 1. Nossa decomposição de portas implementa esse difusor até uma fase global −1. Por isso pode aparecer amplitude −1 em 11; a probabilidade continua 1.

CZ é construída com H no alvo, CNOT e H no alvo. Esse é um exemplo de decomposição: uma operação útil pode ser montada a partir de outras.

## Desafios

1. Remova a etapa do oráculo. O algoritmo ainda favorece 11?
2. Como adaptar somente o oráculo para marcar 00?
3. Por que este experimento não mede vantagem sobre uma busca clássica?

<details><summary>Soluções comentadas</summary>

1. Não. A superposição uniforme permanece uniforme, possivelmente com fase global.
2. Aplique X nos dois qubits antes de CZ e desfaça os X depois. A combinação 00 é temporariamente levada a 11 para receber a fase. Mantenha o difusor original.
3. A resposta foi escolhida na construção do oráculo, o problema tem apenas quatro candidatos e o executor é um simulador clássico. Uma comparação real precisaria contar também construção do oráculo, acesso aos dados e recursos de execução.

</details>

**Antes de seguir:** calcule a média das amplitudes depois do oráculo e obtenha o resultado do difusor no papel.


---

[← Módulo anterior](05-medicao.md) · [Índice](../README.md) · [Próximo módulo →](07-teletransporte.md)
