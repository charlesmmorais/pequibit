# Projeto final — Confiança por comparação

Escolha um circuito de três qubits com pelo menos H, T e CNOT. Escreva-o uma vez em QTG e outra em Qiskit. Aplique as mesmas portas na mesma ordem, respeitando q0 à direita.

Use `software.reference.run` e `Statevector.from_instruction`. Compare com `compare_vectors`. Entregue os dois circuitos, comando para reproduzir, resultado e explicação de uma página.

## Critérios

1. Os estados são equivalentes até fase global, com norma e probabilidades conferidas.
2. O exemplo contém fase complexa e uma operação controlada.
3. Uma alteração proposital de fase relativa faz a comparação detectar a diferença.
4. O relato distingue simulação local, execução física e limitações do teste.

## Pista para começar

Use H 0, T 0 e CNOT 0 2 em três qubits. O estado esperado tem amplitudes 1/√2 em 000 e exp(iπ/4)/√2 em 101. Acrescentar Z 2 a apenas uma versão preserva probabilidades, mas muda a fase relativa; o comparador deve rejeitar a equivalência.

A proposta não inclui medição intermediária: essa comparação precisa tratar ramos, probabilidades e estados condicionais, uma extensão futura.

[Voltar à trilha](README.md).
