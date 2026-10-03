# Roadmap por resultados verificáveis

Não há datas artificiais. Uma etapa termina quando sua evidência existe.

| Marco | Entrega | Critério de conclusão | Estado |
|---|---|---|---|
| M0 — Começar a explorar | Documentação, modelo Python e quatro circuitos | Exemplos executam e testes passam | Implementado nesta base |
| M1 — Números que cabem | Modelo inteiro com escala 16384 | Arredondamento, overflow e erro caracterizados | Planejado |
| M2 — Primeiro núcleo | RTL de dois qubits, H/X/Z/CNOT | Simulação RTL comparada ao modelo inteiro | Planejado |
| M3 — Primeiro resultado físico | UART, top e constraints | Bell e H–H reproduzidos na Tang Nano 20K | Planejado |
| M4 — Oito qubits | Memória e controle parametrizados | Síntese, timing e testes de todos os alvos aprovados | Planejado |
| M5 — Medir e decidir | Amostragem, colapso e controle clássico | Teletransporte passa em todas as ramificações | Planejado |
| M6 — Laboratório ampliado | Fases, Grover e interface de observação | Aulas reproduzíveis e limites medidos | Planejado |

## Primeiras tarefas para issues

1. Definir arredondamento e elaborar exemplos de fronteira do formato inteiro.
2. Implementar modelo inteiro da Hadamard e medir deriva após 100 aplicações.
3. Definir interface síncrona da memória e cronograma de leitura/escrita.
4. Implementar gerador de pares e testar todos os alvos para 2–8 qubits.
5. Implementar núcleo de duas amplitudes e testbench.
6. Identificar revisão da placa e versionar constraints verificadas.
7. Definir pacotes seriais, respostas e tratamento de erros.
8. Registrar primeira execução física com amplitudes e erro numérico.

As tarefas 1–5 antecedem promessas de frequência ou capacidade. HDMI, interface web, SDRAM e integração com Qiskit ficam como expansões, não pré-requisitos do primeiro sucesso.
