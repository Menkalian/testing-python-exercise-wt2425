# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
(After swapping `w` for `h` in the calculation of `nx`)
```
============================= test session starts ==============================
collecting ... collected 6 items

integration/test_diffusion2d.py::test_initialize_physical_parameters 
integration/test_diffusion2d.py::test_set_initial_condition 
unit/test_diffusion2d_functions.py::test_initialize_domain PASSED [ 16%]PASSED       [ 33%]
unit/test_diffusion2d_functions.py::test_initialize_domain_testcase_2 
unit/test_diffusion2d_functions.py::test_initialize_physical_parameters 
unit/test_diffusion2d_functions.py::test_set_initial_condition 

========================= 2 failed, 4 passed in 0.22s ==========================
FAILED        [ 50%]
unit/test_diffusion2d_functions.py:9 (test_initialize_domain)
5 != 10

Expected :10
Actual   :5
<Click to see difference>

def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        # Arrange test values
        w = 20.
        h = 10.
        dx = 2.
        dy = 0.2
    
        # Act (= Perform test action)
        solver.initialize_domain(w, h, dx, dy)
    
        # Assert
        # "cheap" assertions
        assert solver.w == w
        assert solver.h == h
        assert solver.dx == dx
        assert solver.dy == dy
        # Calculated values
>       assert solver.nx == 10
E       assert 5 == 10
E        +  where 5 = <diffusion2d.SolveDiffusion2D object at 0x7fed47f79490>.nx

unit/test_diffusion2d_functions.py:31: AssertionError
FAILED [ 66%]
unit/test_diffusion2d_functions.py:34 (test_initialize_domain_testcase_2)
6 != 5

Expected :5
Actual   :6
<Click to see difference>

def test_initialize_domain_testcase_2():
        """
        Second testcase for function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        # Arrange test values
        # "unschöne" values
        w = 15.2
        h = 17.1
        dx = 2.7
        dy = 0.29
    
        # Act (= Perform test action)
        solver.initialize_domain(w, h, dx, dy)
    
        # Assert
        # "cheap" assertions
        assert solver.w == w
        assert solver.h == h
        assert solver.dx == dx
        assert solver.dy == dy
        # Calculated values
>       assert solver.nx == 5
E       assert 6 == 5
E        +  where 6 = <diffusion2d.SolveDiffusion2D object at 0x7fed47f79a90>.nx

unit/test_diffusion2d_functions.py:57: AssertionError
PASSED [ 83%]dt = 0.0011428571428571432
PASSED    [100%]
Process finished with exit code 1
```

(After changing the formula for `dt`: `dx2, dy2 = self.dx * self.dy, self.dx * self.dy`)
```
============================= test session starts ==============================
collecting ... collected 6 items

integration/test_diffusion2d.py::test_initialize_physical_parameters PASSED [ 16%]
integration/test_diffusion2d.py::test_set_initial_condition PASSED       [ 33%]
unit/test_diffusion2d_functions.py::test_initialize_domain PASSED        [ 50%]
unit/test_diffusion2d_functions.py::test_initialize_domain_testcase_2 PASSED [ 66%]
unit/test_diffusion2d_functions.py::test_initialize_physical_parameters FAILED [ 83%]dt = 0.001428571428571429

unit/test_diffusion2d_functions.py:60 (test_initialize_physical_parameters)
0.001428571428571429 != 0.001142 ± 1.0e-06

Expected :0.001142 ± 1.0e-06
Actual   :0.001428571428571429
<Click to see difference>

def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        # Arrange
        d = 3.5
        T_cold = 342.4
        T_hot = 723.15
        solver.dx = 0.1
        solver.dy = 0.2
    
        # Act
        solver.initialize_physical_parameters(d, T_cold, T_hot)
    
        # Assert
        assert solver.D == d
        assert solver.T_cold == T_cold
        assert solver.T_hot == T_hot
>       assert solver.dt == pytest.approx(0.001142, abs=1e-6)
E       assert 0.001428571428571429 == 0.001142 ± 1.0e-06
E         
E         comparison failed
E         Obtained: 0.001428571428571429
E         Expected: 0.001142 ± 1.0e-06

unit/test_diffusion2d_functions.py:80: AssertionError

unit/test_diffusion2d_functions.py::test_set_initial_condition PASSED    [100%]

========================= 1 failed, 5 passed in 0.22s ==========================

Process finished with exit code 1
```

(After introducing an error into `set_initial_condition` (wrong shape): `u = self.T_cold * np.ones((self.nx, self.nx))`)
```
============================= test session starts ==============================
collecting ... collected 6 items

integration/test_diffusion2d.py::test_initialize_physical_parameters 
integration/test_diffusion2d.py::test_set_initial_condition 
unit/test_diffusion2d_functions.py::test_initialize_domain PASSED [ 16%]PASSED       [ 33%]
unit/test_diffusion2d_functions.py::test_initialize_domain_testcase_2 
unit/test_diffusion2d_functions.py::test_initialize_physical_parameters 
unit/test_diffusion2d_functions.py::test_set_initial_condition 

========================= 1 failed, 5 passed in 0.22s ==========================
PASSED        [ 50%]PASSED [ 66%]PASSED [ 83%]dt = 0.0007142857142857145
FAILED    [100%]
unit/test_diffusion2d_functions.py:82 (test_set_initial_condition)
100 != 50

Expected :50
Actual   :100
<Click to see difference>

def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        # Arrange
        solver.nx = 100
        solver.ny = 50
        solver.dx = 0.1
        solver.dy = 0.2
        solver.T_cold = 100.
        solver.T_hot = 600.
    
        # Act
        u: np.ndarray = solver.set_initial_condition()
    
        # Assert
        # Domain has expected dimensions
        assert u.shape[0] == solver.nx
>       assert u.shape[1] == solver.ny
E       assert 100 == 50
E        +  where 50 = <diffusion2d.SolveDiffusion2D object at 0x7fc72874d340>.ny

unit/test_diffusion2d_functions.py:102: AssertionError

Process finished with exit code 1
```

(After introducing an error into `set_initial_condition` (inverse values): `if not p2 < r2:`)
```
============================= test session starts ==============================
collecting ... collected 6 items

integration/test_diffusion2d.py::test_initialize_physical_parameters 
integration/test_diffusion2d.py::test_set_initial_condition 
unit/test_diffusion2d_functions.py::test_initialize_domain PASSED [ 16%]PASSED       [ 33%]
unit/test_diffusion2d_functions.py::test_initialize_domain_testcase_2 
unit/test_diffusion2d_functions.py::test_initialize_physical_parameters 
unit/test_diffusion2d_functions.py::test_set_initial_condition 

========================= 1 failed, 5 passed in 0.21s ==========================
PASSED        [ 50%]PASSED [ 66%]PASSED [ 83%]dt = 0.0007142857142857145
FAILED    [100%]
unit/test_diffusion2d_functions.py:82 (test_set_initial_condition)
np.float64(600.0) != 100.0

Expected :100.0
Actual   :np.float64(600.0)
<Click to see difference>

def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        # Arrange
        solver.nx = 100
        solver.ny = 50
        solver.dx = 0.1
        solver.dy = 0.2
        solver.T_cold = 100.
        solver.T_hot = 600.
    
        # Act
        u: np.ndarray = solver.set_initial_condition()
    
        # Assert
        # Domain has expected dimensions
        assert u.shape[0] == solver.nx
        assert u.shape[1] == solver.ny
        # Border is cold, center is hot
>       assert u[0][0] == 100.
E       assert np.float64(600.0) == 100.0

unit/test_diffusion2d_functions.py:104: AssertionError

Process finished with exit code 1
```

### unittest log
(After swapping `w` for `h` in the calculation of `nx`)
```
============================= test session starts ==============================
collecting ... collected 4 items

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain FAILED [ 25%]
test_diffusion2d_functions.py:16 (TestDiffusion2D.test_initialize_domain)
10 != 5

Expected :5
Actual   :10
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

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
>       self.assertEqual(self.solver.nx, 10)

test_diffusion2d_functions.py:37: AssertionError

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain_testcase_2 FAILED [ 50%]
test_diffusion2d_functions.py:39 (TestDiffusion2D.test_initialize_domain_testcase_2)
5 != 6

Expected :6
Actual   :5
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain_testcase_2>

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
>       self.assertEqual(self.solver.nx, 5)

test_diffusion2d_functions.py:61: AssertionError

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters PASSED [ 75%]dt = 0.0011428571428571432

test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition PASSED [100%]

========================= 2 failed, 2 passed in 0.21s ==========================

Process finished with exit code 1
```

(After changing the formula for `dt`: `dx2, dy2 = self.dx * self.dy, self.dx * self.dy`)
```
============================= test session starts ==============================
collecting ... collected 4 items

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain PASSED [ 25%]
test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain_testcase_2 PASSED [ 50%]
test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters FAILED [ 75%]dt = 0.001428571428571429

test_diffusion2d_functions.py:63 (TestDiffusion2D.test_initialize_physical_parameters)
self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

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
>       self.assertAlmostEqual(self.solver.dt, 0.001143, 6)
E       AssertionError: 0.001428571428571429 != 0.001143 within 6 places (0.0002855714285714291 difference)

test_diffusion2d_functions.py:83: AssertionError

test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition PASSED [100%]

========================= 1 failed, 3 passed in 0.22s ==========================

Process finished with exit code 1
```

(After introducing an error into `set_initial_condition` (inverse values): `if not p2 < r2:`)
```
============================= test session starts ==============================
collecting ... collected 4 items

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain 
test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain_testcase_2 
test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters 
test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition 

========================= 1 failed, 3 passed in 0.22s ==========================
PASSED [ 25%]PASSED [ 50%]PASSED [ 75%]dt = 0.0011428571428571432
FAILED [100%]
test_diffusion2d_functions.py:84 (TestDiffusion2D.test_set_initial_condition)
100.0 != np.float64(600.0)

Expected :np.float64(600.0)
Actual   :100.0
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

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
>       self.assertEqual(u[0][0], 100.)

test_diffusion2d_functions.py:105: AssertionError

Process finished with exit code 1
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
