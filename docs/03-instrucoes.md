# QTG: uma linguagem pequena para circuitos pequenos

QTG é um formato educativo próprio; não é OpenQASM e não possui compatibilidade automática com Qiskit. As instruções abaixo já funcionam no modelo Python.

| Instrução | Exemplo | Efeito |
|---|---|---|
| INIT n | `INIT 2` | Prepara n qubits em zero; obrigatório no início |
| H q | `H 0` | Porta Hadamard |
| X q | `X 1` | Troca as amplitudes de 0 e 1 no qubit alvo |
| Z q | `Z 0` | Inverte o sinal quando o alvo é 1 |
| S q | `S 0` | Multiplica por i quando o alvo é 1 |
| T q | `T 0` | Multiplica por exp(iπ/4) quando o alvo é 1 |
| CNOT c t | `CNOT 0 1` | Troca o alvo se o controle for 1 |

Linhas vazias e comentários iniciados por `#` são aceitos. Os operandos são inteiros. O modelo limita INIT a 1–12 qubits para evitar alocações acidentais; isso não é uma afirmação sobre a capacidade do hardware. INIT só pode aparecer uma vez.

A saída do programa lista estados com probabilidade maior que 10⁻¹² e depois amostra 1.000 resultados com semente fixa. Isso é amostragem de preparações repetidas, sem colapso do vetor entre amostras. Não existe instrução MEASURE nesta versão.

O hardware inicial implementará apenas o subconjunto INIT, H, X, Z e CNOT. S e T no modelo preparam a futura exploração de fases complexas.
