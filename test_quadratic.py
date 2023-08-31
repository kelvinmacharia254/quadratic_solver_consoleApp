import unittest

import math

from backend_quadratic import Quadratic

class TestQuadratic(unittest.TestCase):
    def test_empty_coeffs(self):
        """
        Test zero coeffs
        """
        input = []
        self.assertEqual(Quadratic(input).error, "Error: No coefficient passed. Atleast one be should be passed.")

    def test_excess_coeffs(self):
        """
        Test excess coeffs
        """
        input = [1,2,1,3]
        self.assertEqual(Quadratic(input).error, f"Error: More than necessary coefficient provided. {len(input)} coeffs provided instead of between 1 to 3 coeffs.")

    def test_bad_types(self):
        """Test bad types"""
        input = ['a', 2, 1]
        self.assertEqual(Quadratic(input).error, "Error: One or more input is non-numeric.")

    def test_one_coeff(self):
        """
        Test one coeff
        """
        input = [1]
        self.assertEqual((math.isclose(Quadratic(input).roots(), 0, rel_tol=1e-02)), True)

    def test_two_coeffs(self):
        """
        Test two coeffs
        """
        input = [5,1]
        self.assertEqual(Quadratic(input).roots(), (0,-0.2))

    def test_three_coeffs(self):
        """
        Test three coeffs,
        """
        input = [1,10,1]
        solution = Quadratic(input).roots()
        for sol, ans in zip(solution,(-0.101, -9.899)):
            self.assertEqual(math.isclose( sol, ans, rel_tol = 1e-02), True)

    def test_three_coeffs_complex_roots(self):
        """
        Test three coeffs
        """
        input = [1,0,1]
        self.assertEqual(Quadratic(input).roots(), ((-0-1j), (-0+1j)))

if __name__ == "__main__":
    unittest.main()
