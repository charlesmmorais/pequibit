import unittest
from software.fixed_reference import FixedCore, rounded_h


class FixedTests(unittest.TestCase):
    def test_known_rounding_and_ties(self):
        self.assertEqual(rounded_h(16384), 11585)
        self.assertEqual(rounded_h(-16384), -11585)
        # 11585 * 8192 / 16384 = 5792.5; empate afasta de zero.
        self.assertEqual(rounded_h(8192), 5793)
        self.assertEqual(rounded_h(-8192), -5793)
        self.assertEqual(rounded_h(0), 0)

    def test_bell_and_norm(self):
        core = FixedCore()
        self.assertFalse(core.execute(1))
        self.assertFalse(core.execute(4, target=1, control=0))
        self.assertEqual(core.state, [(11585, 0), (0, 0), (0, 0), (11585, 0)])
        norm = sum(x*x for pair in core.state for x in pair)/16384**2
        self.assertLess(abs(norm-1), 1e-4)

    def test_complex_hadamard(self):
        core = FixedCore()
        core.state = [(0, 16384), (0, 0), (0, 0), (0, 0)]
        core.execute(1, target=1)
        self.assertEqual(core.state, [(0, 11585), (0, 0), (0, 11585), (0, 0)])

    def test_overflow_is_atomic(self):
        for op in (1, 3):
            core = FixedCore()
            core.state = [(-32768, -32768)]*4
            before = core.state.copy()
            self.assertTrue(core.execute(op))
            self.assertEqual(core.state, before)

    def test_invalid_opcode_and_control(self):
        core = FixedCore()
        for opcode, target, control in [(6,0,0), (7,0,0), (4,0,0), (4,1,1)]:
            before = core.state.copy()
            self.assertTrue(core.execute(opcode, target, control))
            self.assertEqual(core.state, before)

    def test_basis_swaps_and_z(self):
        for basis in range(4):
            for target in (0, 1):
                core = FixedCore()
                core.state = [(0, 0)]*4
                core.state[basis] = (16384, 0)
                core.execute(2, target)
                self.assertEqual(core.state[basis ^ (1<<target)], (16384, 0))
                core.execute(2, target)
                core.execute(3, target)
                self.assertEqual(core.state[basis], (-16384 if basis & (1<<target) else 16384, 0))
