"""Testes de previsões físicas e contratos de entrada do modelo educativo."""
import math
import unittest
from pathlib import Path
from software.reference import StateVector, run


class ReferenceTests(unittest.TestCase):
    def assert_state(self, state, expected):
        self.assertEqual(len(state.amplitudes), len(expected))
        for actual, target in zip(state.amplitudes, expected):
            self.assertLess(abs(actual - target), 1e-12)

    def test_hadamard(self):
        s = 1 / math.sqrt(2)
        self.assert_state(run('INIT 1\nH 0'), [s, s])

    def test_interference(self):
        self.assert_state(run('INIT 1\nH 0\nH 0'), [1, 0])
        self.assert_state(run('INIT 1\nH 0\nZ 0\nH 0'), [0, 1])

    def test_bell_and_inverse(self):
        s = 1 / math.sqrt(2)
        circuit = 'INIT 2\nH 0\nCNOT 0 1'
        self.assert_state(run(circuit), [s, 0, 0, s])
        self.assert_state(run(circuit + '\nCNOT 0 1\nH 0'), [1, 0, 0, 0])

    def test_cnot_all_basis_states_and_directions(self):
        for control, target in [(0, 1), (1, 0)]:
            for basis in range(4):
                state = StateVector(2)
                state.amplitudes = [0j] * 4
                state.amplitudes[basis] = 1
                state.cnot(control, target)
                result = basis ^ (1 << target) if basis & (1 << control) else basis
                expected = [0] * 4
                expected[result] = 1
                self.assert_state(state, expected)

    def test_complex_phase(self):
        s = 1 / math.sqrt(2)
        self.assert_state(run('INIT 1\nH 0\nS 0'), [s, 1j*s])
        self.assert_state(run('INIT 1\nH 0\nT 0\nT 0'), [s, 1j*s])
        self.assert_state(run('INIT 1\nH 0\nS 0\nS 0'), [s, -s])

    def test_norm_and_inverse_each_target(self):
        state = StateVector(8)
        for target in range(8):
            state.gate('H', target)
            state.gate('T', target)
        self.assertAlmostEqual(sum(state.probabilities()), 1, places=12)
        for target in range(8):
            before = state.amplitudes.copy()
            state.gate('X', target)
            state.gate('X', target)
            self.assert_state(state, before)

    def test_sampling_is_reproducible_and_does_not_collapse(self):
        state = run('INIT 2\nH 0\nCNOT 0 1')
        before = state.amplitudes.copy()
        counts = state.sample()
        self.assertEqual(counts, state.sample())
        self.assertEqual(sum(counts.values()), 1000)
        self.assertEqual(set(counts), {'00', '11'})
        self.assert_state(state, before)
        self.assertEqual(run('INIT 1\nX 0').sample(), {'1': 1000})

    def test_invalid_input(self):
        for source in ['', 'H 0', 'INIT 0', 'INIT 13', 'INIT 2\nCNOT 0 0',
                       'INIT 1\nH 1', 'INIT 1\nX -1', 'INIT 1\nH',
                       'INIT 1\nFOO 0', 'INIT 1\nINIT 2', 'INIT a']:
            with self.subTest(source=source), self.assertRaises(ValueError):
                run(source)

    def test_published_examples(self):
        folder = Path(__file__).resolve().parents[1] / 'examples'
        expected = {'01_hadamard.qtg': [.5, .5],
                    '02_interference.qtg': [1, 0],
                    '03_bell.qtg': [.5, 0, 0, .5],
                    '04_phase.qtg': [0, 1]}
        for name, probabilities in expected.items():
            state = run((folder / name).read_text())
            for actual, target in zip(state.probabilities(), probabilities):
                self.assertAlmostEqual(actual, target, places=12)


if __name__ == '__main__':
    unittest.main()
