import numpy as np
from astropy.modeling import models,fitting

def find_minimum(x, y):
    ''' This is our fitter function using which we can plot FWHM (y var) versus focus step (x var).
    Our inputs are the columns with focus step and FWHM, assuming these are in columns zero (x) and
    one (y) of our arrays
    Parameters
    ----------


    Returns
    -------

    '''
    fit_parabola
    find_vertex
    return

def fit_parabola(x, y):
    '''This finds the coefficients of the fit parabola.
    Step 1: looking for parabola
    Step 2: get linear least square fitting
    Step 3: execute
    Step 4: store coefficients in an array.

    Parameters
    ----------

    Returns
    -------

    '''

    t_init = models.Polynomial1D(2)
    fitter = fitting.LinearLSQFitter()
    t_fit = fitter(t_init, x, y)
    a = t_fit.c2.value
    b = t_fit.c1.value
    c = t_fit.c0.value
    coefficients = np.array([a, b, c])

    return coefficients

def find_vertex(coefficients):
    '''Once we have the fit, the vertex is required.
    Using the formula of a parabola vertex we can get
    the optimal focus length.

    Parameters
    ----------


    Returns
    -------

    '''
    a = coefficients[0]
    b = coefficients[1]

    return -b/(2*a)
