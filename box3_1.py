# Box 3.1 from page 26.

import numpy as np
import matplotlib.pyplot as plt

# Define parameters of hemodynamic response function (hrf).
t0 = 0 		#
n = 4 		#
lamda = 2	#

# Define the time axis.
time = np.arange(0,30.01,.01)  # from 0 to 30 sec in 1 msec increments

# Define the hrf.
from hrf import hrf

# Plot the hrf.
plt.plot(time,hrf(t0, time, n, lamda))
plt.show()