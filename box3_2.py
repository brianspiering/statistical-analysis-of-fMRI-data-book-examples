import math
import numpy as np
import matplotlib.pyplot as plt

# Define parameters of hemodynamic response function (hrf).
t0 = 0
n = 4
lamda = 2

# Define the time axis. 
time = np.arange(0,50,.01) # 0 to 50 sec in 1 msec increments

# Define the 3 boxcar functions.
null=[0]*50000 #[zeros(1,5000);]
box5=[1]*500 + [0]*4500 #[ones(1,500),zeros(1,4501)];
box20=[0]*2000 + [0]*3000 #[ones(1,2000),zeros(1,3001)];
box50=[1]*5000 # [ones(1,5000),0];

# Create the hrf
hrf = ((time-t0)**(n-1))**np.exp(-(time-t0)/lamda)/((lamda**n)*math.factorial(n-1)) # Works but is not right. See box3_1.py

# Compute the 3 convolutions. Divide by 100 to set time unit at .01 sec.
bold5 = np.convolve(box5, hrf, mode='same') # BOLD5=conv(box5,hrf)/100;
bold20 = np.convolve(box20, hrf, mode='same') # conv(box20,hrf)/100;
bold50 = np.convolve(box50, hrf, mode='same') # conv(box50,hrf)/100;

#  Plot the predicted BOLD response
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
ax1.plot(time, bold5)
ax2.scatter(time, bold20)
ax3.scatter(time, bold50)
plt.show()