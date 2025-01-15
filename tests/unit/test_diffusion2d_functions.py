"""
Tests for functions in class SolveDiffusion2D
"""
from unittest import TestCase

import numpy as np
import unittest

from diffusion2d import SolveDiffusion2D


class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        # Arrange test values
        w = 20.
        h = 10.
        dx = 2.
        dy = 0.2

        # Act (= Perform test action)
        self.solver.initialize_domain(w, h, dx, dy)

        # Assert
        # "cheap" assertions
        self.assertEqual(self.solver.w, w)
        self.assertEqual(self.solver.h, h)
        self.assertEqual(self.solver.dx, dx)
        self.assertEqual(self.solver.dy, dy)
        # Calculated values
        self.assertEqual(self.solver.nx, 10)
        self.assertEqual(self.solver.ny, 50)

    def test_initialize_domain_testcase_2(self):
        """
        Second testcase for function SolveDiffusion2D.initialize_domain
        """
        # Arrange test values
        # "unschöne" values
        w = 15.2
        h = 17.1
        dx = 2.7
        dy = 0.29

        # Act (= Perform test action)
        self.solver.initialize_domain(w, h, dx, dy)

        # Assert
        # "cheap" assertions
        self.assertEqual(self.solver.w, w)
        self.assertEqual(self.solver.h, h)
        self.assertEqual(self.solver.dx, dx)
        self.assertEqual(self.solver.dy, dy)
        # Calculated values
        self.assertEqual(self.solver.nx, 5)
        self.assertEqual(self.solver.ny, 58)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        # Arrange
        d = 3.5
        T_cold = 342.4
        T_hot = 723.15
        self.solver.dx = 0.1
        self.solver.dy = 0.2

        # Act
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)

        # Assert
        self.assertEqual(self.solver.D, d)
        self.assertEqual(self.solver.T_cold, T_cold)
        self.assertEqual(self.solver.T_hot, T_hot)
        # unittest assumes rounding here, so the last decimal differs from pytest.
        self.assertAlmostEqual(self.solver.dt, 0.001143, 6)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        # Arrange
        self.solver.nx = 100
        self.solver.ny = 50
        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.T_cold = 100.
        self.solver.T_hot = 600.

        # Act
        u: np.ndarray = self.solver.set_initial_condition()

        # Assert
        # Domain has expected dimensions
        self.assertEqual(u.shape[0], self.solver.nx)
        self.assertEqual(u.shape[1], self.solver.ny)
        # Border is cold, center is hot
        self.assertEqual(u[0][0], 100.)
        self.assertEqual(u[99][0], 100.)
        self.assertEqual(u[0][49], 100.)
        self.assertEqual(u[99][49], 100.)

        self.assertEqual(u[49][24], 600.)
        self.assertEqual(u[50][24], 600.)
        self.assertEqual(u[49][25], 600.)
        self.assertEqual(u[50][25], 600.)

if __name__ == '__main__':
    unittest.main()