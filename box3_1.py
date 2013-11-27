# Box 3.1 from page 26.

from numpy import arange
from matplotlib.pyplot import plot, show

# Define parameters of hemodynamic response function (hrf).
T0 = 0 	# Lag between stimulus presentation and inital BOLD rise
n = 4 		# a hrf shape parameter
lamda = 2	# a hrf shape parameter

# Define the time axis.
time = arange(0,30.01,.01)  # from 0 to 30 sec in 1 msec increments

# Define the hrf.
from hrf import hrf

# Plot the hrf.
plot(time,hrf(T0, time, n, lamda))
show()