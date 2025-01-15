"""
Tests for functionality checks in class SolveDiffusion2D
"""
import pytest

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(10., 20., 0.2, 0.1)
    solver.initialize_physical_parameters(2.4, 0., 1.)
    # dx2 = 0.04
    # dy2 = 0.01
    # dt = 0.0004 / (2*2.4*0.05) = 1/600 = 0.0016666
    assert solver.dt == pytest.approx(0.001666, abs=1e-6)


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(10., 10., 1., 1.)
    solver.initialize_physical_parameters(2.7, 0., 1.)
    u = solver.set_initial_condition()

    expected_array= [
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 1., 1., 0., 0., 0.],
        [0., 0., 0., 0., 1., 1., 1., 0., 0., 0.],
        [0., 0., 0., 0., 1., 1., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
    ]

    for x in range(u.shape[0]):
        for y in range(u.shape[1]):
            assert expected_array[x][y] == u[x, y], f"Values at {x}, {y} do not match"
