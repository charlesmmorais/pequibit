# Evidências da primeira implementação RTL

Data: 3 de outubro de 2026.

## Executado localmente

- Python 3.12: 24 testes do núcleo e curso básico aprovados, incluindo seis testes do modelo inteiro.
- Icarus Verilog 12.0: 812 comandos comparados bit a bit com o modelo de ponto fixo.
- Testbench: reset durante comando, operandos capturados no aceite, comando concorrente ignorado durante busy, pulsos done/error e timeout.
- Casos numéricos: Bell, inversão, entradas da base, dois alvos, CNOT nos dois sentidos, componentes imaginárias, valores extremos, empates de arredondamento, overflow e opcodes inválidos.
- Yosys 0.33: síntese genérica concluída e `check -assert` sem problemas. A saída genérica possui 12.257 células primitivas no total hierárquico; esse número não equivale a LUTs Gowin e não comprova ocupação na Tang Nano.

## Ainda não executado

Síntese para o dispositivo Gowin, place-and-route, análise temporal da placa, validação de pinagem, comunicação serial e execução física. Nenhuma frequência máxima ou capacidade de expansão foi medida.

O modelo e o RTL seguem o mesmo contrato. Para reduzir risco de erro comum, testes analíticos verificam Bell, arredondamento e transformações de base separadamente. Isso não é prova formal de correção para todas as entradas.
