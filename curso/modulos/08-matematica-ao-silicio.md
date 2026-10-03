# 8. Da matemática ao silício

**Pergunta:** quanto de uma amplitude cabe em dezesseis bits?

**Objetivo:** entender quantização e planejar o primeiro bloco de hardware. Reserve 60 minutos. Esta aula é executável no computador; a integração física da FPGA permanece planejada.

O modelo ideal usa números complexos de ponto flutuante. A proposta para a FPGA representa cada componente por um inteiro de 16 bits com sinal e escala 16384: o valor real é inteiro/16384. Assim, 16384 representa +1, −16384 representa −1, e 11585 aproxima 1/√2.

Uma amplitude tem componente real e imaginária: quatro bytes no total. Um estado de oito qubits possui 256 amplitudes e precisa de 1024 bytes, sem contar buffers e controle.

## Veja o erro aparecer

Execute `python3 -m curso.experimentos ponto-fixo`.

A demonstração quantiza o coeficiente de H e arredonda os resultados. Ela imprime as amplitudes e a norma ao quadrado após 1, 2 e 100 aplicações. Compare o retorno esperado a |0⟩ depois de duas H com o valor aproximado obtido.

Esta função usa inteiros Python sem limite de largura, divisão em ponto flutuante e `round` com empate para o par. Não é o modelo bit a bit do RTL: serve para tornar a quantização visível. Overflow, larguras intermediárias e regras de arredondamento do hardware precisam ser especificados separadamente.

## Desenhe seu primeiro bloco

Um bloco de Hadamard recebe a e b, calcula soma e diferença, multiplica pela constante e escreve a' e b'. Os dois operandos devem ser lidos antes da escrita. A memória pode demandar vários ciclos; não presuma que toda a operação ocorre em um único clock.

Escreva a interface no papel: entradas, saídas, sinal de início, sinal de término e indicação de erro. Depois descreva uma sequência de ciclos que não sobrescreva um operando ainda necessário.

## Desafios

1. Quantos bytes um vetor de dez qubits precisa nessa representação?
2. Por que somar dois inteiros de 16 bits pode exigir 17 bits?
3. Por que renormalizar todo resultado pode esconder um defeito?

<details><summary>Soluções comentadas</summary>

1. 2¹⁰×4=4096 bytes, ou 4 KiB.
2. A soma pode exceder a faixa dos operandos; a largura intermediária precisa preservar o resultado antes da conversão.
3. A renormalização pode mascarar crescimento ou perda indevida de norma por erro de cálculo. Primeiro medimos e explicamos a deriva.

</details>

**Projeto final:** siga o [roteiro](../projeto-final.md). A síntese e a gravação da Tang Nano 20K pertencem aos próximos marcos do projeto, não são necessárias para concluir este curso introdutório.


---

[← Módulo anterior](07-teletransporte.md) · [Índice](../README.md) · [Projeto final →](../projeto-final.md)

Para avançar além da demonstração, veja o [núcleo implementado e seu modelo inteiro](../../hardware/README.md).
