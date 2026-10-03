"""Contrato inteiro do núcleo de dois qubits; escala 16384, sem floats."""
SCALE = 16384
H_COEFFICIENT = 11585
MIN_VALUE, MAX_VALUE = -32768, 32767


def rounded_h(value):
    product = value * H_COEFFICIENT
    magnitude = (abs(product) + SCALE//2)//SCALE
    return -magnitude if product < 0 else magnitude


class FixedCore:
    def __init__(self):
        self.state = [(SCALE, 0), (0, 0), (0, 0), (0, 0)]

    def execute(self, opcode, target=0, control=0, address=0, real=0, imag=0):
        """Devolve True para erro; nesse caso o vetor permanece inalterado."""
        if target not in (0, 1) or control not in (0, 1):
            raise ValueError('O núcleo possui apenas q0 e q1.')
        candidate = self.state.copy()
        if opcode == 0:
            candidate = [(SCALE, 0), (0, 0), (0, 0), (0, 0)]
        elif opcode == 1:
            for first in range(4):
                if not first & (1 << target):
                    second = first | (1 << target)
                    a, b = self.state[first], self.state[second]
                    candidate[first] = tuple(rounded_h(x+y) for x, y in zip(a, b))
                    candidate[second] = tuple(rounded_h(x-y) for x, y in zip(a, b))
        elif opcode == 2:
            candidate = [self.state[index ^ (1 << target)] for index in range(4)]
        elif opcode == 3:
            candidate = [tuple(-x for x in pair) if index & (1 << target) else pair
                         for index, pair in enumerate(self.state)]
        elif opcode == 4:
            if target == control:
                return True
            candidate = [self.state[index ^ (1 << target)] if index & (1 << control)
                         else self.state[index] for index in range(4)]
        elif opcode == 5:
            if not 0 <= address < 4:
                raise ValueError('Endereço fora da memória de quatro amplitudes.')
            candidate[address] = (real, imag)
        else:
            return True
        if any(not MIN_VALUE <= x <= MAX_VALUE for pair in candidate for x in pair):
            return True
        self.state = candidate
        return False
