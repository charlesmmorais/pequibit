# Vamos construir uma explicação que funcione

Comece por uma mudança pequena. Se uma frase confundiu você, conte onde e o que esperava entender. Não é preciso dominar física quântica para contribuir.

## Escrita

Use português simples, defina cada termo na primeira ocorrência e explique o motivo de uma decisão. Separe fatos, hipóteses, propostas e resultados medidos. Toda aula deve trazer uma pergunta, um experimento, um resultado esperado e uma limitação. Evite “faz todas as contas ao mesmo tempo”, “comunicação instantânea” e promessas de quebra de criptografia.

## Código

Nomes de funções e sinais em inglês; comentários didáticos em português. Prefira funções pequenas, módulos com uma responsabilidade e dependências explícitas. Documente convenção de bits, unidades, larguras e arredondamento. Não inclua bitstreams ou relatórios enormes sem necessidade.

## Uma contribuição completa

Descreva o problema, a alteração e como verificou. Execute `python3 -m unittest discover -s tests -v`. Alterações em RTL deverão incluir testbench e comparação numérica quando essa etapa existir. Não atribua validação física a resultados obtidos apenas em simulação.

Trate dúvidas com respeito. Corrija ideias com evidências e ajude a pessoa a reproduzir o resultado.
