"""Verificações analíticas dos novos experimentos e da medição."""
import math
import random
import subprocess
import sys
import unittest
from pathlib import Path
from curso.experimentos import grover, teleport, receiver_fidelity, fixed_h_pair
from software.reference import run


class CourseTests(unittest.TestCase):
    def test_measurement_collapses_and_repeats(self):
        for seed in range(30):
            state = run('INIT 2\nH 0\nCNOT 0 1')
            rng = random.Random(seed)
            bit = state.measure(0, rng)
            self.assertEqual(state.measure(0, rng), bit)
            self.assertEqual(state.measure(1, rng), bit)
            expected = [0] * 4
            expected[3 if bit else 0] = 1
            for actual, target in zip(state.probabilities(), expected):
                self.assertAlmostEqual(actual, target, places=12)

    def test_each_branch_normalization_and_weight(self):
        for bit in (0, 1):
            state = run('INIT 2\nH 0\nCNOT 0 1')
            self.assertAlmostEqual(state.collapse(0, bit), .5, places=12)
            self.assertAlmostEqual(sum(state.probabilities()), 1, places=12)

    def test_impossible_branch_preserves_state(self):
        state = run('INIT 1')
        before = state.amplitudes.copy()
        with self.assertRaises(ValueError):
            state.collapse(0, 1)
        self.assertEqual(state.amplitudes, before)
        for args in [(-1, 0), (1, 0), (0, 2)]:
            with self.assertRaises(ValueError):
                state.collapse(*args)
        with self.assertRaises(ValueError):
            state.measure(1)

    def test_grover_marks_11(self):
        state = grover()
        for actual, target in zip(state.probabilities(), [0, 0, 0, 1]):
            self.assertAlmostEqual(actual, target, places=12)

    def test_teleport_all_branches_and_complex_inputs(self):
        s = 1/math.sqrt(2)
        inputs = [(1+0j, 0j), (0j, 1+0j), (s+0j, s+0j),
                  (s+0j, -s+0j), (s+0j, 1j*s),
                  (complex(math.sqrt(3)/2), .5j)]
        for alpha, beta in inputs:
            for m0 in (0, 1):
                for m1 in (0, 1):
                    with self.subTest(input=(alpha, beta), branch=(m0, m1)):
                        state, bits, weight = teleport(alpha, beta, branch=(m0, m1))
                        self.assertEqual(bits, (m0, m1))
                        self.assertAlmostEqual(weight, .25, places=12)
                        self.assertAlmostEqual(sum(state.probabilities()), 1, places=12)
                        self.assertAlmostEqual(receiver_fidelity(state, alpha, beta), 1, places=12)
                        # Verificação independente: razão das amplitudes do ramo final.
                        index = m0 | (m1 << 1)
                        self.assertLess(abs(state.amplitudes[index]*beta
                                            - state.amplitudes[index | 4]*alpha), 1e-12)

    def test_random_teleport_and_validation(self):
        alpha, beta = complex(math.sqrt(3)/2), .5j
        for seed in range(20):
            state, _, _ = teleport(alpha, beta, seed=seed)
            self.assertAlmostEqual(receiver_fidelity(state, alpha, beta), 1, places=12)
        with self.assertRaises(ValueError):
            teleport(1, 1)

    def test_fidelity_detects_wrong_relative_phase(self):
        state = run('INIT 3\nH 2\nS 2')
        s = 1/math.sqrt(2)
        self.assertAlmostEqual(receiver_fidelity(state, complex(s), -1j*s), 0, places=12)

    def test_fixed_point_demonstration(self):
        self.assertEqual(fixed_h_pair(16384, 0), (11585, 11585))
        a, b = fixed_h_pair(11585, 11585)
        self.assertEqual(b, 0)
        self.assertLess(abs(a/16384 - 1), 2/16384)

    def test_course_commands(self):
        root = Path(__file__).resolve().parents[1]
        for name in ['medicao', 'grover', 'teletransporte', 'ponto-fixo']:
            result = subprocess.run([sys.executable, '-m', 'curso.experimentos', name],
                                    cwd=root, capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(result.stdout.strip())
