# Box 3.1 from page 26.

import math
import numpy as np
import matplotlib.pyplot as plt

# Define parameters of hemodynamic response function (hrf).
t0 = 0 		#
n = 4 		#
lamda = 2	#

# Define the time axis.
time = np.arange(0,30.01,.01)  # from 0 to 30 sec in 1 msec increments

# Define the hrf.
hrf = ((time-t0)**(n-1))**np.exp(-(time-t0)/lamda)/((lamda**n)*
math.factorial(n-1)) 
# TODO: confirm shape; create module version

# Plot the hrf.
plt.plot(time,hrf)
 # axis([0 30 0 .12]);
plt.show()