# Verificação da implementação do curso

Data: 3 de outubro de 2026. Python 3.12.

A suíte `python3 -m unittest discover -s tests -v`, executada na raiz do projeto, passou com **18 testes**. A implementação preserva os nove testes originais e acrescenta nove testes para os experimentos e contratos de medição.

Cobertura específica: colapso e repetibilidade, normalização e peso dos ramos, rejeição de pós-seleção impossível sem alteração do estado, Grover, seis estados de entrada do teletransporte nos quatro ramos, execuções sorteadas, detecção de fase relativa incorreta, exemplo de quantização e os quatro comandos do curso executados em subprocessos.

Os seis estados incluem 0, 1, +, −, +i e uma superposição assimétrica com fase complexa. As verificações usam tolerância de 10⁻¹² no modelo ideal. Isso não constitui tolerância já validada para hardware de ponto fixo.

Todos os links relativos da documentação foram conferidos. O exemplo de ponto fixo é apenas ilustrativo, sem emulação completa de larguras ou overflow. Não houve execução em FPGA nem processador quântico físico.
