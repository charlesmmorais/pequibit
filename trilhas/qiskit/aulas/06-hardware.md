# 6. Preparar um circuito para outro conjunto de portas

**Pergunta:** a máquina precisa executar exatamente as portas que escrevemos?

**Objetivo:** conhecer transpilação, conectividade e ruído sem depender de uma conta na nuvem. Tempo sugerido: 45–60 minutos.

O exemplo usa `transpile` para reescrever Bell na base abstrata `rz`, `sx`, `x`, `cx`. Ele imprime contagens antes e depois e compara os operadores completos com `Operator.equiv`. Isso verifica a ação em qualquer entrada, até fase global, para este pequeno circuito.

Uma porta H pode virar uma sequência de outras operações. Transpilar não torna um circuito automaticamente mais rápido: o resultado depende das restrições e do objetivo de otimização.

## Conectividade

Uma QPU pode permitir portas de dois qubits apenas entre certos pares. O compilador pode introduzir operações para mover informação entre posições. Imagine três posições em linha, 0–1–2: uma interação entre 0 e 2 pode exigir roteamento. É necessário acompanhar o mapeamento final dos qubits antes de comparar saídas.

O exemplo executável desta aula transforma apenas a base de portas. Não impõe um mapa de conexões e não representa uma QPU específica.

## Ruído

`Statevector` neste curso descreve evolução ideal. Erros de portas, leitura e decoerência exigem modelos adicionais. Uma contagem sorteada que se afasta de 50% não é, por si só, uma simulação de ruído do dispositivo.

## Desafios

1. Compare contagens de portas antes e depois de transpilar. Uma quantidade maior significa automaticamente menor qualidade?
2. O resultado “operadores equivalentes” prova que o circuito funcionará com fidelidade 1 em uma QPU?

<details><summary>Soluções comentadas</summary>

1. Não. Precisamos considerar portas disponíveis, duração, erros e restrições de conectividade.
2. Não. A equivalência é matemática e ideal. O comportamento físico requer execução, calibração e análise de erros.

</details>

**Próximo passo:** estudar um backend real e suas condições de acesso. Esta trilha não instala Qiskit Runtime, solicita credenciais, envia trabalhos à nuvem ou grava a Tang Nano. A base escolhida aqui também não é o conjunto de instruções da FPGA proposta.


## Executar o exemplo da aula

Na raiz do repositório, com o ambiente virtual ativado:

```bash
python -m trilhas.qiskit.experimentos transpilar
```

[← Anterior](05-grover.md) · [Índice](../README.md) · [Projeto final →](../projeto-final.md)
