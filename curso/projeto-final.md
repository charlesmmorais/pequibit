# Projeto final — Uma experiência que você consegue explicar

## Missão

Crie uma pequena demonstração que outra pessoa consiga reproduzir. Entregue um circuito ou script e um relato de uma página: pergunta, previsão, procedimento, resultado e limites.

Escolha uma opção:

1. **Interferência:** compare H–H, H–Z–H e H–S–H. Explique amplitudes, fases e probabilidades.
2. **Busca:** adapte o oráculo de Grover para marcar 00 e confira que a resposta muda.
3. **Teletransporte:** verifique as entradas 0, 1 e (√3/2)|0⟩+(i/2)|1⟩ nos quatro ramos. Registre fidelidade e probabilidades.
4. **Engenharia:** compare a quantização de H em três escalas e apresente erro de norma após várias aplicações. Deixe explícito que isso não é síntese de hardware.

## Critérios de conclusão

| Critério | Evidência |
|---|---|
| Execução | Comando, versão de Python e código disponíveis |
| Previsão | Resultado esperado escrito antes da execução |
| Correção | Teste numérico que verificaria um erro real |
| Explicação | Relação entre operações e resultado em suas palavras |
| Honestidade científica | Limites da simulação e da experiência declarados |

Considere concluído quando atender aos cinco critérios. Resultado inesperado não é fracasso: documentar e explicar um erro é parte do trabalho.

## Pistas e resultados para autocorreção

- H–S–H produz probabilidades 1/2 e 1/2, enquanto H–H produz 0 e H–Z–H produz 1 de forma determinística.
- Para marcar 00, envolva somente CZ com X nos dois qubits. Não altere o difusor.
- Para cada entrada normalizada de teletransporte, os quatro ramos corrigidos têm fidelidade 1 e peso 1/4 no caso ideal.
- Na quantização, compare com o resultado ideal da mesma quantidade de portas. Reporte a escala e o arredondamento; não conclua que uma placa suporta um circuito apenas porque o script terminou.

[Voltar ao curso](README.md).
