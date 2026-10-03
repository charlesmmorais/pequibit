# Laboratórios: pergunte, preveja, execute, explique

Cada atividade deve caber em uma sessão curta. Antes de executar, escreva sua previsão. Se ela não bater com o resultado, encontramos uma boa pergunta para investigar.

## 1. Uma porta, duas possibilidades — implementado no modelo

Execute `python3 software/reference.py examples/01_hadamard.qtg`.

Pergunta: o que muda depois de H? Esperado: amplitudes 1/√2 para 0 e 1, probabilidades de 50%. Experimento: altere a semente no modelo e observe as contagens, sem mudar as probabilidades calculadas. Não interprete diferenças de contagem como erro da porta.

## 2. A segunda porta desfaz a primeira — implementado no modelo

Execute `python3 software/reference.py examples/02_interference.qtg`.

Pergunta: duas portas H tornam o resultado “mais aleatório”? Esperado: probabilidade aproximadamente 1 para 0. Explique usando soma e subtração de amplitudes. A aproximação numérica pode deixar resíduos muito pequenos.

## 3. Dois qubits, um estado conjunto — implementado no modelo

Execute `python3 software/reference.py examples/03_bell.qtg`.

Esperado: amplitudes 1/√2 em 00 e 11; zero nas demais. Os resultados individuais variam, mas os dois bits são iguais em cada amostra ideal.

Teste adicional: depois de preparar Bell, aplique CNOT 0 1 e H 0. O resultado deve voltar a 00. Esse teste examina coerência; uma simples tabela de probabilidades sem fase não basta para reproduzi-lo.

## 4. Uma fase que aparece depois — implementado no modelo

Execute `python3 software/reference.py examples/04_phase.qtg`.

O circuito H–Z–H equivale a X. Esperado: resultado 1. Compare com H–H. A fase introduzida por Z passa a afetar probabilidades após a última H.

## 5. Grover de dois qubits — planejado

Objetivo: marcar 11 e amplificar sua probabilidade com uma iteração. Implementar CZ por H no alvo, CNOT, H no alvo. Conferir a distribuição final e explicar por que o oráculo contém uma regra de reconhecimento. Esta atividade não demonstra uma vantagem prática de busca em uma lista de quatro elementos.

## 6. Teletransporte — planejado

Objetivo: transferir um estado simulado de q0 para q2 com três qubits e dois bits clássicos. Preparar estados de teste que incluam fases complexas. Verificar as quatro ramificações das medições, as correções e a fidelidade final. O estado original não permanece como uma cópia utilizável. Nenhuma matéria ou mensagem superluminal é transferida.

## Do computador à placa

Repetir os primeiros quatro laboratórios com o futuro executor FPGA. Registrar circuito, revisão da placa, versão do compilador, commit, clock, amplitudes e erro em relação ao modelo. A experiência só muda de status após essa evidência.
