"""Experimentos do curso: execute com python -m curso.experimentos NOME."""
import argparse
import math
import random
from software.reference import StateVector, run


def grover():
    """Uma iteração, dois qubits e oráculo que marca 11."""
    return run('''INIT 2
H 0
H 1
# CZ = H no alvo, CNOT, H no alvo
H 1
CNOT 0 1
H 1
# Difusor, equivalente até uma fase global
H 0
H 1
Z 0
Z 1
H 1
CNOT 0 1
H 1
H 0
H 1
''')


def teleport(alpha, beta, seed=42, branch=None):
    """Transfere alpha|0>+beta|1> de q0 para q2.

    branch=(m0,m1) permite estudar uma ramificação por pós-seleção.
    Sem branch, as medições são sorteadas. Devolve estado, bits e peso do ramo.
    """
    if not math.isclose(abs(alpha)**2 + abs(beta)**2, 1, abs_tol=1e-12, rel_tol=0):
        raise ValueError('O estado de entrada deve estar normalizado.')
    state = StateVector(3)
    # Inicialização matemática do estado conhecido para esta experiência.
    state.amplitudes[0], state.amplitudes[1] = alpha, beta
    state.gate('H', 1)
    state.cnot(1, 2)
    state.cnot(0, 1)
    state.gate('H', 0)
    rng = random.Random(seed)
    if branch is None:
        m0 = state.measure(0, rng)
        m1 = state.measure(1, rng)
        weight = 0.25  # Cada ramo do protocolo ideal tem probabilidade 1/4.
    else:
        m0, m1 = branch
        weight = state.collapse(0, m0) * state.collapse(1, m1)
    if m1:
        state.gate('X', 2)
    if m0:
        state.gate('Z', 2)
    return state, (m0, m1), weight


def receiver_fidelity(state, alpha, beta):
    """Probabilidade da projeção de q2 no estado de entrada, ignorando q1/q0."""
    return sum(abs(alpha.conjugate() * state.amplitudes[low]
                   + beta.conjugate() * state.amplitudes[low | 4])**2
               for low in range(4))


def fixed_h_pair(a, b, scale=16384):
    """Demonstração de quantização; não é ainda o modelo bit a bit da FPGA."""
    coefficient = round(scale / math.sqrt(2))
    return (round((a+b)*coefficient/scale), round((a-b)*coefficient/scale))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment', choices=['medicao', 'grover', 'teletransporte', 'ponto-fixo'])
    args = parser.parse_args()
    if args.experiment == 'medicao':
        state = run('INIT 1\nH 0')
        print('Probabilidades antes:', state.probabilities())
        print('Amostras sem alterar o vetor:', dict(state.sample(1000, 42)))
        rng = random.Random(42)
        first = state.measure(0, rng)
        print('Primeira medição:', first)
        print('Probabilidades após colapso:', state.probabilities())
        print('Segunda medição sem nova porta:', state.measure(0, rng))
    elif args.experiment == 'grover':
        state = grover()
        print('Probabilidades [00, 01, 10, 11]:', state.probabilities())
        print('Amostras:', dict(state.sample()))
    elif args.experiment == 'teletransporte':
        alpha, beta = complex(1/math.sqrt(2)), complex(0, 1/math.sqrt(2))
        state, bits, _ = teleport(alpha, beta)
        print('Entrada: (|0> + i|1>)/sqrt(2)')
        print('Bits clássicos (m0, m1):', bits)
        print(f'Fidelidade de q2: {receiver_fidelity(state, alpha, beta):.12f}')
        print('Verificação didática por pós-seleção dos quatro ramos:')
        for branch in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            state, _, weight = teleport(alpha, beta, branch=branch)
            print(branch, f'P={weight:.6f}', f'F={receiver_fidelity(state, alpha, beta):.12f}')
    else:
        scale = 16384
        a, b = scale, 0
        print('Escala:', scale, 'aproximação inteira de 1/sqrt(2):', round(scale/math.sqrt(2)))
        for step in range(1, 101):
            a, b = fixed_h_pair(a, b, scale)
            if step in (1, 2, 100):
                print(f'H aplicado {step} vez(es): amplitudes={(a/scale, b/scale)}, norma²={(a*a+b*b)/scale**2:.9f}')
        print('Modelo ilustrativo: sem largura limitada, saturação ou detecção de overflow.')


if __name__ == '__main__':
    main()
