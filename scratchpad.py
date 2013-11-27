## Debugging test_hrf

time = arange(0,10,1)
n = 4

# ((time-t0)**(n-1))**exp(-(time-t0)/lamda)/((lamda**n)*factorial(n-1))


## Define parameters of hemodynamic response function (hrf).
#T0 = 0 	# Lag between stimulus presentation and inital BOLD rise
#n = 4 		# a hrf shape parameter
#lamda = 2	# a hrf shape parameter
# 
# 
## Define the time axis.
#from numpy import arange
#time = arange(0, 30.01, .01)  # from 0 to 30 sec in 1 msec increments 
# 
#from hrf import hrf
#
#hrf(T0, time, n, lamda)