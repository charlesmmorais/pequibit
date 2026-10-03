# Ciência que pode ser conferida

## Três níveis de comparação

1. **Matemática:** vetores conhecidos e identidades de portas, usando complexo em ponto flutuante.
2. **Aritmética digital:** modelo inteiro com as mesmas larguras, escala e arredondamento do RTL.
3. **Placa:** saída física comparada ao resultado do modelo inteiro para o mesmo programa.

Esta base cobre o primeiro nível. Os outros níveis estão planejados.

## O que verificar

- H duas vezes e X duas vezes restauram o estado.
- Z muda fase sem mudar imediatamente a probabilidade computacional.
- CNOT visita e troca os endereços corretos para ambos os sentidos de controle.
- Bell seguido do circuito inverso retorna a 00.
- S² = Z e T² = S, inclusive com amplitudes complexas.
- A norma é preservada dentro da tolerância numérica.
- Entradas inválidas falham com uma mensagem compreensível.

Na comparação física entre estados, uma fase global não altera previsões observáveis. Para estados normalizados, usar fidelidade |⟨ψref|ψteste⟩|²; também medir norma antes de qualquer normalização. Para comparar RTL com seu modelo inteiro, exigir igualdade bit a bit.

## Tolerâncias

Os testes analíticos de pequenos circuitos no modelo Python usam tolerância de 10⁻¹². Esse limite não se aplica ao formato de 16 bits. Para o hardware, caracterizar erro por profundidade e quantidade de qubits antes de fixar tolerâncias. Não declarar sucesso apenas porque um histograma “parece certo”.

## Amostragem

As sementes tornam o teste reproduzível; não tornam os resultados quânticos físicos. Não exigir exatamente 500/500 em mil amostras. Testar suporte, soma de contagens e comportamento em estados determinísticos; avaliações estatísticas mais amplas devem declarar amostra, tolerância e probabilidade de falso alarme.

## Evidência de hardware

Publicar revisão da placa, ferramentas e versões, commit, clock solicitado e atingido, uso de LUT/BSRAM/DSP, violações de timing, circuito, contagens ou amplitudes e procedimento de reprodução. Nenhum desses resultados foi medido nesta entrega.
