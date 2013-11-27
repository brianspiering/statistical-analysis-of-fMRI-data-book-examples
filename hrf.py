# TODO: confirm values

from numpy import exp
from math import factorial

def hrf(t0, time, n, lamda):
    return ((time-t0)**(n-1))**exp(-(time-t0)/lamda)/((lamda**n)*factorial(n-1))