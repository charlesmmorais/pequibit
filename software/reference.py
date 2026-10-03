"""Modelo educativo ideal. q0 é o bit menos significativo; não há FPGA aqui."""
import argparse
import cmath
import math
import random
from collections import Counter
from pathlib import Path


class StateVector:
    def __init__(self, qubits):
        if not 1 <= qubits <= 12:
            raise ValueError('Use entre 1 e 12 qubits no modelo educativo.')
        self.qubits = qubits
        self.amplitudes = [0j] * (1 << qubits)
        self.amplitudes[0] = 1 + 0j

    def check_qubit(self, qubit):
        if not 0 <= qubit < self.qubits:
            raise ValueError(f'Qubit {qubit} fora do circuito.')

    def gate(self, name, target):
        self.check_qubit(target)
        scale = 1 / math.sqrt(2)
        matrices = {
            'H': ((scale, scale), (scale, -scale)),
            'X': ((0, 1), (1, 0)),
            'Z': ((1, 0), (0, -1)),
            'S': ((1, 0), (0, 1j)),
            'T': ((1, 0), (0, cmath.exp(1j * math.pi / 4))),
        }
        if name not in matrices:
            raise ValueError(f'Porta desconhecida: {name}')
        matrix = matrices[name]
        mask = 1 << target
        for first in range(len(self.amplitudes)):
            if first & mask:
                continue
            second = first | mask
            # Ler os dois valores antes de escrever evita destruir um operando.
            a, b = self.amplitudes[first], self.amplitudes[second]
            self.amplitudes[first] = matrix[0][0] * a + matrix[0][1] * b
            self.amplitudes[second] = matrix[1][0] * a + matrix[1][1] * b

    def cnot(self, control, target):
        self.check_qubit(control)
        self.check_qubit(target)
        if control == target:
            raise ValueError('Controle e alvo devem ser diferentes.')
        for first in range(len(self.amplitudes)):
            if first & (1 << control) and not first & (1 << target):
                second = first | (1 << target)
                self.amplitudes[first], self.amplitudes[second] = (
                    self.amplitudes[second], self.amplitudes[first])

    def collapse(self, target, outcome):
        """Seleciona uma ramificação para análise; retorna sua probabilidade.

        Isto é pós-seleção matemática, não controle físico de um resultado.
        Um resultado impossível é rejeitado antes de alterar o vetor.
        """
        self.check_qubit(target)
        if outcome not in (0, 1):
            raise ValueError('O resultado deve ser 0 ou 1.')
        probability = sum(abs(a) ** 2 for index, a in enumerate(self.amplitudes)
                          if ((index >> target) & 1) == outcome)
        if probability <= 0:
            raise ValueError('Não é possível selecionar uma ramificação de probabilidade zero.')
        divisor = math.sqrt(probability)
        self.amplitudes = [a / divisor if ((index >> target) & 1) == outcome else 0j
                           for index, a in enumerate(self.amplitudes)]
        return probability

    def measure(self, target, rng=None):
        """Mede um qubit na base computacional e colapsa o estado conjunto."""
        self.check_qubit(target)
        rng = rng if rng is not None else random.Random()
        weights = [sum(abs(a) ** 2 for index, a in enumerate(self.amplitudes)
                       if ((index >> target) & 1) == bit) for bit in (0, 1)]
        outcome = rng.choices((0, 1), weights=weights, k=1)[0]
        self.collapse(target, outcome)
        return outcome

    def probabilities(self):
        return [abs(amplitude) ** 2 for amplitude in self.amplitudes]

    def sample(self, shots=1000, seed=42):
        """Amostra preparações repetidas; não colapsa o vetor armazenado."""
        if shots < 1:
            raise ValueError('O número de amostras deve ser positivo.')
        rng = random.Random(seed)
        outcomes = rng.choices(range(len(self.amplitudes)),
                               weights=self.probabilities(), k=shots)
        return Counter(format(value, f'0{self.qubits}b') for value in outcomes)


def run(source):
    state = None
    arities = {'INIT': 1, 'H': 1, 'X': 1, 'Z': 1, 'S': 1, 'T': 1, 'CNOT': 2}
    for line_number, raw in enumerate(source.splitlines(), 1):
        tokens = raw.split('#', 1)[0].split()
        if not tokens:
            continue
        name, *arguments = tokens
        try:
            if name not in arities or len(arguments) != arities[name]:
                raise ValueError('Instrução desconhecida ou quantidade de operandos incorreta.')
            operands = [int(value) for value in arguments]
            if name == 'INIT':
                if state is not None:
                    raise ValueError('INIT só pode aparecer uma vez.')
                state = StateVector(operands[0])
            elif state is None:
                raise ValueError('Comece o circuito com INIT.')
            elif name == 'CNOT':
                state.cnot(*operands)
            else:
                state.gate(name, operands[0])
        except ValueError as error:
            raise ValueError(f'Linha {line_number}: {error}') from error
    if state is None:
        raise ValueError('Circuito vazio: inclua INIT.')
    return state


def main():
    parser = argparse.ArgumentParser(description='Pequibit: explore um circuito ideal.')
    parser.add_argument('circuit', type=Path)
    args = parser.parse_args()
    try:
        state = run(args.circuit.read_text(encoding='utf-8'))
    except (OSError, ValueError) as error:
        parser.exit(2, f'Erro: {error}\n')
    print('Estado calculado (q0 à direita):')
    for index, probability in enumerate(state.probabilities()):
        if probability > 1e-12:
            label = format(index, f'0{state.qubits}b')
            print(f'|{label}> amplitude={state.amplitudes[index]:.8f} P={probability:.8f}')
    print('1000 amostras, semente 42:', dict(sorted(state.sample().items())))


if __name__ == '__main__':
    main()
