"""Suíte opcional: falha se Qiskit não estiver instalado, sem skips silenciosos."""
import random
import subprocess
import sys
import unittest
from pathlib import Path
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator
from software.reference import StateVector
from trilhas.qiskit.experimentos import compare_vectors, compare_examples, grover, compile_example


class QiskitComparisonTests(unittest.TestCase):
    def test_published_examples(self):
        for name, result in compare_examples().items():
            with self.subTest(name=name):
                self.assertTrue(result['equivalent'])
                self.assertLess(result['probability_error'], 1e-12)
                self.assertLess(result['norm_error'], 1e-12)

    def test_global_phase_accepted_relative_phase_rejected(self):
        s = 2**-.5
        self.assertTrue(compare_vectors([s, s], [-s, -s])['equivalent'])
        result = compare_vectors([s, s], [s, -s])
        self.assertFalse(result['equivalent'])
        self.assertAlmostEqual(result['probability_error'], 0)
        with self.assertRaises(ValueError):
            compare_vectors([1, 0], [1, 0, 0, 0])

    def test_bit_order_and_cnot_directions(self):
        for control, target in [(0, 1), (1, 0)]:
            for basis in range(4):
                circuit = QuantumCircuit(2)
                local = StateVector(2)
                for bit in range(2):
                    if basis & (1 << bit):
                        circuit.x(bit)
                        local.gate('X', bit)
                circuit.cx(control, target)
                local.cnot(control, target)
                self.assertTrue(compare_vectors(local.amplitudes,
                    Statevector.from_instruction(circuit).data)['equivalent'])

    def test_seeded_circuits_with_complex_phases(self):
        rng = random.Random(19)
        for qubits in (1, 2, 3, 5):
            circuit, local = QuantumCircuit(qubits), StateVector(qubits)
            for _ in range(40):
                gate = rng.choice(['H', 'X', 'Z', 'S', 'T', 'CNOT'] if qubits > 1
                                  else ['H', 'X', 'Z', 'S', 'T'])
                if gate == 'CNOT':
                    control, target = rng.sample(range(qubits), 2)
                    circuit.cx(control, target)
                    local.cnot(control, target)
                else:
                    target = rng.randrange(qubits)
                    getattr(circuit, gate.lower())(target)
                    local.gate(gate, target)
            result = compare_vectors(local.amplitudes, Statevector.from_instruction(circuit).data)
            self.assertTrue(result['equivalent'])
            self.assertLess(result['norm_error'], 1e-12)

    def test_grover_analytic_answer(self):
        probabilities = Statevector.from_instruction(grover()).probabilities()
        for actual, expected in zip(probabilities, [0, 0, 0, 1]):
            self.assertAlmostEqual(actual, expected, places=12)

    def test_transpilation_preserves_operator(self):
        original, compiled = compile_example()
        self.assertTrue(Operator(original).equiv(Operator(compiled)))
        self.assertTrue(set(compiled.count_ops()) <= {'rz', 'sx', 'x', 'cx'})

    def test_all_course_commands(self):
        root = Path(__file__).resolve().parents[1]
        for experiment in ['primeiro', 'hadamard', 'bell', 'comparar', 'grover', 'transpilar']:
            result = subprocess.run([sys.executable, '-m', 'trilhas.qiskit.experimentos', experiment],
                                    cwd=root, capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
