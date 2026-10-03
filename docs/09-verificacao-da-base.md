# Verificação desta entrega

Data: 3 de outubro de 2026.

Ambiente: Python 3.12, execução local a partir da raiz do projeto.

Comando: `python3 -m unittest discover -s tests -v`.

Resultado: **9 testes aprovados**, abrangendo Hadamard, interferência, Bell e inversão, CNOT nas duas direções e em todas as entradas de dois qubits, fases complexas, norma, amostragem e entradas inválidas. Os quatro exemplos publicados foram conferidos pelos testes.

A execução direta de Bell calculou P(00)=0,5 e P(11)=0,5. A amostragem com semente 42 produziu 480 resultados 00 e 520 resultados 11 em mil preparações simuladas. A diferença é compatível com a natureza da amostragem e não muda as probabilidades calculadas.

A suíte do GitHub está configurada, mas ainda não foi executada no serviço remoto. Não houve síntese, simulação RTL ou execução em FPGA. O modelo não foi comparado nesta entrega com Qiskit; os testes usam previsões analíticas.
