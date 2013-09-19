# TODO: confirm values

import numpy as np
import math

def hrf(t0, time, n, lamda):
    return ((time-t0)**(n-1))**np.exp(-(time-t0)/lamda)/((lamda**n)*
    math.factorial(n-1))