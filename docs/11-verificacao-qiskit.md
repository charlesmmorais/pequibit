# Verificação da trilha Qiskit

Data: 3 de outubro de 2026. Ambiente local: Python 3.12 e Qiskit 2.2.3 em ambiente virtual separado.

- 18 testes do núcleo/curso básico passaram no ambiente sem Qiskit.
- 7 testes opcionais passaram no ambiente com Qiskit.
- Os seis comandos publicados nas aulas foram executados por testes em subprocessos.
- Foram comparados os quatro circuitos originais e Grover, além de circuitos com semente fixa, fases complexas e CNOT nas duas direções.
- A transpilação foi verificada por equivalência do operador completo no exemplo pequeno, até fase global.
- Os links relativos da documentação foram conferidos.

A tolerância de 10⁻¹² vale para os exemplos locais em ponto flutuante. Não caracteriza precisão da futura FPGA. A comparação Qiskit não inclui teletransporte ou medição intermediária nesta versão. Não houve execução em QPU, simulação de ruído ou gravação da placa.

O workflow contém dois jobs: o básico sem dependências opcionais e o de Qiskit, que instala requirements-qiskit.txt. A suíte opcional falha se a dependência faltar, em vez de marcar testes como pulados.
