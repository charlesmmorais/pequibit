# Pequibit com Qiskit — Da descoberta à programação

Uma trilha opcional para repetir experimentos conhecidos em outra ferramenta, comparar resultados e aprender a preparar circuitos para diferentes conjuntos de portas.

**Pré-requisito:** módulos 1–6 do [curso básico](../../curso/README.md), ou conhecimento equivalente de amplitudes, fase, Bell e Grover. Reserve 5–7 horas com exercícios e projeto. Não é necessário ter FPGA, conta IBM ou acesso a uma QPU.

## Ambiente de estudo

Use Python 3.12, a versão de referência dos testes desta trilha. Todos os comandos partem da raiz do repositório.

Linux/macOS:

```bash
python3 -m venv .venv-qiskit
source .venv-qiskit/bin/activate
```

Windows PowerShell:

```powershell
py -3.12 -m venv .venv-qiskit
.venv-qiskit\Scripts\Activate.ps1
```

Se o PowerShell impedir a ativação, use diretamente `.venv-qiskit\Scripts\python.exe` no lugar de `python` nos comandos seguintes; não é necessário alterar a política do sistema.

```bash
python -m pip install -r requirements-qiskit.txt
python -m trilhas.qiskit.experimentos primeiro
python -m unittest discover -s tests_qiskit -v
```

Fixamos **Qiskit 2.2.3** como referência didática, sem afirmar que seja a versão mais recente. O ambiente virtual mantém essa dependência separada do curso inicial. As dependências transitivas são resolvidas pelo pip; este arquivo não é um lock completo do ambiente.

## Aulas

| Aula | Experimento |
|---|---|
| [1. Seu primeiro circuito em Qiskit](aulas/01-primeiro-circuito.md) | `primeiro` |
| [2. Probabilidades e amostras](aulas/02-hadamard.md) | `hadamard` |
| [3. Dois qubits em um estado conjunto](aulas/03-bell.md) | `bell` |
| [4. Dois simuladores, uma previsão](aulas/04-comparacao.md) | `comparar` |
| [5. Grover com portas de alto nível](aulas/05-grover.md) | `grover` |
| [6. Preparar um circuito para outro conjunto de portas](aulas/06-hardware.md) | `transpilar` |

## Duas suítes, dois propósitos

```bash
# Continua funcionando sem Qiskit:
python -m unittest discover -s tests -v
# Requer a instalação opcional:
python -m unittest discover -s tests_qiskit -v
```

A suíte opcional não silencia a falta de Qiskit com testes pulados. No GitHub Actions, cada suíte tem um job separado, e apenas o job da trilha instala a dependência.

## O que observar

Preveja o resultado antes de executar. Registre amplitudes, probabilidades e contagens separadamente. Não espere as mesmas contagens com a mesma semente entre bibliotecas: os geradores podem ser diferentes. Compare distribuições e equivalência até fase global.

Os exemplos usam somente recursos locais. Não há conversor geral de formatos, integração com QPU ou executor FPGA nesta trilha.

- [Projeto final](projeto-final.md)
- [Fontes e dúvidas](referencias.md)
- [Código dos experimentos](experimentos.py)
