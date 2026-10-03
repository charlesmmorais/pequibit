# Do cadastro ao primeiro teste no computador quântico da IBM

**Um laboratório Pequibit para sair da simulação e conhecer uma QPU real.**

Você criará uma conta, escolherá o plano gratuito, testará Bell no computador e aprenderá a enviar o circuito à IBM. A preparação local leva aproximadamente 30–60 minutos; cadastro e fila podem levar mais tempo. Não é necessário ter uma Tang Nano 20K.

**Documentação conferida em 3 de outubro de 2026.** Telas e condições comerciais podem mudar; confira os links oficiais ao seguir o guia. O fluxo de cadastro foi descrito a partir da documentação, não de uma conta criada durante a elaboração deste material.

## 1. Entenda as quatro peças

| Peça | Para que serve |
|---|---|
| IBMid/login | Sua identidade para entrar na plataforma |
| Conta IBM Cloud | Contexto de recursos e permissões |
| Instância | Recurso associado a um plano, identificado por um CRN |
| API key | Credencial que permite ao programa autenticar-se |

Ter um login não significa que você já tenha uma instância pronta para executar circuitos.

## 2. Crie a conta

1. Abra a [IBM Quantum Platform](https://quantum.cloud.ibm.com/) e procure a opção de cadastro ou entrada.
2. Use sua identidade existente ou siga a criação de IBMid. A documentação também apresenta entrada com Google; siga as opções oferecidas na sua tela.
3. Complete as etapas de cadastro e verificações solicitadas. Se faltar uma conta IBM Cloud, use o [cadastro indicado pela IBM](https://quantum.cloud.ibm.com/registration).
4. Ao entrar no painel, confira a conta selecionada no cabeçalho. Uma pessoa pode ter acesso a mais de uma conta.

**Ponto de chegada:** você consegue abrir o painel da plataforma e localizar **Instances**. Se o cadastro pedir validações adicionais, siga a orientação da IBM; este guia não promete ausência de verificação de identidade ou de dados de pagamento.

Fonte: [configuração da conta](https://quantum.cloud.ibm.com/docs/en/guides/cloud-setup).

## 3. Crie uma instância gratuita

1. Selecione a região **us-east** no cabeçalho.
2. Abra **Instances → Create instance**.
3. Dê um nome descritivo, por exemplo `pequibit-open`.
4. Escolha **Open**, o plano gratuito. O nome que você deu à instância não determina o plano.
5. Avance pelas telas de recursos e acesso, revise e conclua em **Create instance**.
6. Abra a instância e copie seu **CRN** completo. Confira se o plano exibido é Open.

Se já existir uma instância Open acessível, você pode utilizá-la. Se a opção Open não aparecer, confira conta, região e permissões antes de continuar. Não selecione Pay-As-You-Go para “destravar” este tutorial gratuito.

Fonte: [instâncias e seus planos](https://quantum.cloud.ibm.com/docs/en/guides/instances).

## 4. Como funciona o Open Plan

| Pergunta | Resposta |
|---|---|
| É gratuito? | O Open oferece acesso gratuito dentro da cota e condições vigentes. |
| Qual é a cota padrão? | Até **10 minutos de QPU por janela móvel de 28 dias**. |
| Reinicia no dia 1º? | Não: a janela acompanha os últimos 28 dias. |
| Onde pode ser criado? | Na região **us-east**. |
| Como acompanhar? | Pelo painel da plataforma e pelos trabalhos em Workloads. |

A documentação cita uma promoção opcional de 180 minutos adicionais para usuários elegíveis. Não contamos com ela neste laboratório; veja no painel se está disponível e quais são os termos.

Fonte: [planos oficiais](https://quantum.cloud.ibm.com/docs/en/guides/plans-overview).

O consumo é ligado ao período em que a QPU fica reservada para executar o trabalho, incluindo custos operacionais associados. Não é o tempo que você passa estudando nem todo o tempo aguardando na fila. Cancelar depois de começar não garante consumo zero. Consulte o uso real depois da execução; não existe uma conversão universal de “1024 shots” em segundos.

Fonte: [medição de consumo](https://quantum.cloud.ibm.com/docs/en/guides/estimate-job-run-time).

Usaremos **job mode**, enviando um trabalho independente. O Open não admite trabalhos em Session. Fonte: [Sampler](https://quantum.cloud.ibm.com/docs/en/guides/get-started-with-sampler).

## 5. Prepare um ambiente separado

Baixe ou atualize o repositório [Pequibit](https://github.com/charlesmmorais/pequibit). Abra o terminal na raiz, onde estão `requirements-ibm.txt` e `laboratorios`.

Use Python 3.12. Este laboratório fixa Qiskit 2.5.2 e Runtime 0.47.0; a trilha introdutória continua com seu próprio ambiente Qiskit 2.2.3. Não instale os dois arquivos de requisitos no mesmo ambiente.

Linux/macOS:

```bash
python3 -m venv .venv-ibm
source .venv-ibm/bin/activate
python -m pip install -r requirements-ibm.txt
```

Windows PowerShell:

```powershell
py -3.12 -m venv .venv-ibm
.venv-ibm\Scripts\Activate.ps1
python -m pip install -r requirements-ibm.txt
```

Se a ativação for bloqueada no Windows, substitua `python` por `.venv-ibm\Scripts\python.exe` nos comandos, sem mudar a política do sistema.

Essas versões usam `from qiskit_ibm_runtime import SamplerV2`. A documentação mais nova também apresenta um cliente a partir de Runtime 0.50; não misture imports de versões diferentes sem atualizar e testar o ambiente.

## 6. Faça o ensaio local — sem conta e sem consumo

```bash
python -m laboratorios.ibm.bell --saida resultados-ibm/bell-local.json
```

O script prepara Bell com H em q0 e CNOT de q0 para q1, acrescenta as medições e sorteia 1024 resultados localmente. Esperamos apenas `00` e `11`, aproximadamente metade de cada. A saída `modo: simulacao_local` deixa claro que nenhuma QPU foi usada.

Abra o JSON e confira `shots_observados`, `contagens` e `fracao_bits_iguais`. No caso ideal, a fração de bits iguais será 1. O programa rejeita um nome de arquivo já existente; escolha outro para uma nova experiência.

## 7. Obtenha sua API key

No painel inicial, localize a criação de **API key**. Gere a chave e guarde-a em um local seguro; ela pode não ser exibida novamente. Tenha também o CRN da instância Open.

Nosso script pede a chave com entrada oculta no terminal. Ela não vai para o código, para o JSON ou para o histórico de comandos. Não cole a chave em issues, prints, commits ou nesta conversa. O script não salva credenciais em disco.

A IBM também oferece `save_account()` para persistência local em computadores confiáveis; este primeiro roteiro opta pela entrada a cada conexão. Fonte: [credenciais](https://quantum.cloud.ibm.com/docs/en/guides/save-credentials).

## 8. Envie um único teste à QPU

```bash
python -m laboratorios.ibm.bell --enviar --shots 1024 --saida resultados-ibm/bell-envio.json
```

O programa pedirá a API key e o CRN. Ele conecta explicitamente à instância informada, procura uma QPU operacional acessível e transpila o circuito para ela. Depois mostra o nome da máquina e pede `ENVIAR OPEN`.

**Antes de digitar:** confirme no painel que o CRN copiado corresponde ao Open. O script não consulta o tipo de plano e não pode garantir gratuidade apenas pelo nome da instância. Se o CRN for de um plano pago, sua execução pode consumir esse plano.

Após confirmar, será enviado um job. O identificador aparece no terminal e no JSON. Guarde-o. O programa termina após o envio para que você possa acompanhar a fila sem manter o terminal aberto.

Conexão usada: `QiskitRuntimeService(channel='ibm_quantum_platform', token=..., instance=...)`. A indicação explícita da instância evita depender da seleção automática entre planos. Fonte: [inicialização do serviço](https://quantum.cloud.ibm.com/docs/en/guides/initialize-account).

## 9. Consulte sem reenviar

Abra **Workloads** na plataforma ou execute, substituindo `ID_DO_JOB` pelo identificador recebido:

```bash
python -m laboratorios.ibm.bell --job ID_DO_JOB --saida resultados-ibm/bell-qpu.json
```

A consulta pede novamente chave e CRN, mas não cria outro job. Se ainda não terminou, informa o estado e sai sem criar o arquivo de resultados. Consulte mais tarde. Se terminou com sucesso, coleta as contagens e salva o relatório.

Se aparecer FAILED, ERROR ou CANCELLED, veja a mensagem detalhada em Workloads. Se perdeu a conexão depois de enviar e antes de anotar o ID, procure o trabalho no painel antes de repetir `--enviar`.

## 10. Interprete o resultado

| Observação | Interpretação |
|---|---|
| 00 e 11 dominam | Resultado compatível com a correlação esperada de Bell |
| Aparecem 01 e 10 | Podem refletir erros de preparação, portas ou leitura |
| 00 e 11 não são exatamente iguais | Pode haver flutuação estatística e efeitos do dispositivo |
| Fração de bits iguais menor que 1 | A correlação observada difere da previsão ideal |

A fração de bits iguais **não é fidelidade do estado** e não prova entrelaçamento. Uma mistura clássica de 00 e 11 também teria fração 1. Um laboratório posterior pode incluir medições em X e Y e uma testemunha de entrelaçamento, considerando incertezas e erros de medição.

Registre data, versões, backend, job ID, shots, contagens e consumo exibido no painel. Compare o JSON local com o da QPU, sem esperar igualdade literal entre amostras.

## 11. Problemas frequentes

| Sintoma | O que conferir |
|---|---|
| 401 / autenticação | API key correta, válida, sem espaços; não use senha ou bearer token no lugar da chave |
| 403 / acesso negado | Permissão da conta para a instância informada |
| Instância não aparece | Conta selecionada e região us-east |
| Nenhuma QPU disponível | Acesso do plano, manutenção e disponibilidade; tente consultar depois |
| Cota insuficiente | Uso na janela móvel; não migre de plano automaticamente |
| Erro de Session | Use o script em job mode |
| `No module named ...` | Ambiente virtual ativo e instalação do requirements-ibm.txt |
| Arquivo de saída já existe | Escolha outro nome; o script preserva o relatório anterior |

## O que foi e o que não foi validado

Os circuitos, imports e modo local são testados sem credenciais. O fluxo remoto segue as APIs documentadas, mas não foi executado em uma conta IBM nem em uma QPU durante a criação deste guia. O primeiro resultado real será o obtido por você após o envio autorizado no seu terminal.

Código: [laboratório Bell](../laboratorios/ibm/bell.py). Voltar à [trilha Qiskit](../trilhas/qiskit/README.md).
