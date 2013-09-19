import numpy as np
import random

# Define x.
x = np.ones(shape=(20,20))*5        # define entire area
x[5:14,5:14] = x[5:14,5:14] + 7     # "raise" section
x[5:8,5:8] = x[5:8,5:8] + 5         # "raise" section
x[9:11,9:11] = x[9:11,9:11] + 35    # "raise" section
x[12:14,12:14] = x[12:14,12:14]+27  # "raise" section
n = random.normalvariate(0,1.5)     # TODO: make it 20x20 array