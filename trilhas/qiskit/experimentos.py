"""Exemplos locais da trilha opcional de Qiskit; nenhuma chamada à nuvem."""
import argparse
from pathlib import Path

try:
    from qiskit import QuantumCircuit, transpile
    from qiskit.quantum_info import Operator, Statevector
except ModuleNotFoundError as error:
    if error.name == 'qiskit':
        raise SystemExit('Instale a trilha: python -m pip install -r requirements-qiskit.txt') from error
    raise

from software.reference import run
from curso.experimentos import grover as pequibit_grover


def bell():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    return circuit


def grover():
    """Construção independente: CZ nativa e difusor padrão com X."""
    circuit = QuantumCircuit(2)
    circuit.h([0, 1])
    circuit.cz(0, 1)
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.cz(0, 1)
    circuit.x([0, 1])
    circuit.h([0, 1])
    return circuit


def compare_vectors(reference, candidate):
    """Compara probabilidades, norma e estado até uma fase global."""
    reference, candidate = Statevector(reference), Statevector(candidate)
    if reference.dim != candidate.dim:
        raise ValueError('Os vetores devem ter a mesma dimensão.')
    norm_error = max(abs(sum(abs(a)**2 for a in vector.data) - 1)
                     for vector in (reference, candidate))
    probability_error = max(abs(a-b) for a, b in
                            zip(reference.probabilities(), candidate.probabilities()))
    equivalent = bool(reference.equiv(candidate, rtol=0, atol=1e-12))
    return {'equivalent': equivalent, 'probability_error': float(probability_error),
            'norm_error': float(norm_error)}


def compare_examples():
    """Fixtures independentes em QTG e Qiskit: não é um conversor de formatos."""
    root = Path(__file__).resolve().parents[2]
    h = QuantumCircuit(1)
    h.h(0)
    interference = QuantumCircuit(1)
    interference.h(0)
    interference.h(0)
    phase = QuantumCircuit(1)
    phase.h(0)
    phase.z(0)
    phase.h(0)
    pairs = [('01_hadamard.qtg', h), ('02_interference.qtg', interference),
             ('03_bell.qtg', bell()), ('04_phase.qtg', phase)]
    results = {}
    for filename, circuit in pairs:
        pequibit = run((root / 'examples' / filename).read_text(encoding='utf-8'))
        results[filename] = compare_vectors(pequibit.amplitudes,
                                           Statevector.from_instruction(circuit).data)
    results['grover'] = compare_vectors(pequibit_grover().amplitudes,
                                        Statevector.from_instruction(grover()).data)
    return results


def compile_example():
    circuit = bell()
    # Alvo didático abstrato: não representa uma QPU ou a Tang Nano.
    compiled = transpile(circuit, basis_gates=['rz', 'sx', 'x', 'cx'],
                         optimization_level=1, seed_transpiler=42)
    return circuit, compiled


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment', choices=['primeiro', 'hadamard', 'bell', 'comparar', 'grover', 'transpilar'])
    args = parser.parse_args()
    if args.experiment == 'comparar':
        results = compare_examples()
        for name, result in results.items():
            print(name, result)
        if not all(r['equivalent'] and r['norm_error'] < 1e-12
                   and r['probability_error'] < 1e-12 for r in results.values()):
            raise SystemExit('Comparação falhou.')
        return
    if args.experiment == 'transpilar':
        original, compiled = compile_example()
        print('Operações originais:', dict(original.count_ops()))
        print('Operações após transpilar:', dict(compiled.count_ops()))
        print('Operadores equivalentes:', Operator(original).equiv(Operator(compiled)))
        print('Alvo abstrato: não houve execução em hardware.')
        return
    if args.experiment in ('primeiro', 'hadamard'):
        circuit = QuantumCircuit(1)
        getattr(circuit, 'x' if args.experiment == 'primeiro' else 'h')(0)
    else:
        circuit = bell() if args.experiment == 'bell' else grover()
    state = Statevector.from_instruction(circuit)
    state.seed(42)
    print('Portas:', dict(circuit.count_ops()))
    print('Amplitudes:', state.data)
    print('Probabilidades:', state.probabilities_dict())
    print('1000 amostras:', state.sample_counts(1000))


if __name__ == '__main__':
    main()
