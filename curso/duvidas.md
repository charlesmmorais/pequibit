# Quando alguma coisa não funciona

**O terminal diz que não encontra `software` ou `curso`.** Abra o terminal na raiz do repositório, a pasta que contém esses diretórios. Os experimentos usam `python3 -m curso.experimentos ...`.

**Python não foi encontrado.** Instale Python 3.10 ou superior e confira `python3 --version`. No Windows, tente `py -3 --version` e use esse comando nos exemplos.

**As amostras não deram exatamente metade para cada resultado.** Isso é esperado. Compare probabilidades calculadas e contagens; variar a semente muda as contagens, não o circuito.

**Apareceu −1 onde eu esperava +1.** Verifique se é uma fase global de todo o estado ou uma fase relativa. No Grover desta implementação, o difusor tem uma fase global em relação à forma padrão.

**A fidelidade deu 0,9999999999999998.** É um resíduo de ponto flutuante próximo de 1; use tolerância numérica. Isso não é medida de ruído físico.

**A medição sempre dá o mesmo resultado.** Uma semente fixa repete uma execução. Medir novamente um estado já colapsado sem uma nova porta também repete o resultado. Para novos ensaios, prepare o circuito novamente e reutilize um gerador que avance sua sequência.

**Posso gravar isso na Tang Nano agora?** Ainda não. O curso usa um modelo executável; o núcleo RTL está simulado, mas a integração da placa segue pendente no roadmap.

**O comando MEASURE não funciona no QTG.** Nesta versão, medição está disponível na API Python como `measure`, não no parser QTG.

[Voltar ao curso](README.md).
