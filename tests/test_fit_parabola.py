from focuser import fit_parabola
import pytest
import numpy as np


def parabola(x, parameters):
    return parameters[0] + parameters[1]*x + parameters[2]*x**2


def test_find_minimum_nonoise():
    parameters = [4, 3, 2]  # c0, c1, c2

    x = np.arange(10)
    y = parabola(x, parameters)
    expected = -parameters[1]/(2*parameters[2])

    minimum = fit_parabola.find_minimum(x, y)
    assert minimum == pytest.approx(expected)


def test_find_minimum_yesnoise():
    parameters = [-20, 47, 42]  # c0, c1, c2

    np.random.seed(5)
    n = 10
    x = np.arange(n)
    y = parabola(x, parameters) + np.random.normal(size=n)
    expected = -parameters[1]/(2*parameters[2])

    minimum = fit_parabola.find_minimum(x, y)
    assert minimum == pytest.approx(expected, abs=1e-3)
