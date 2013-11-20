# Test Box 3_1.py

# TODO: Refactor to generalize to all files
# Learn TDD

import os
import scipy.io

def load_matlab_data_file(directory, filename):
    os.chdir(directory) # change to data dir
    return scipy.io.loadmat(file_name) # load data file
    
# Load MATLAB data, aka the ground truth
directory = os.getcwd() + '/matlab_data/'
file_name = 'box3_1'

current_mat = load_matlab_data_file(directory, file_name)

# Run Python script
# TODO: import box3_1.py

# Compare
