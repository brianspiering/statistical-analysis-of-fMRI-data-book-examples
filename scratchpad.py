import os
import scipy.io
import numpy as np

# Load MATLAB file
def load_matlab_data_file(directory, filename):
    return scipy.io.loadmat(directory + filename) # load MATLAB file into dict

directory = os.getcwd()  + '/matlab_files/'
current_file_name = 'box3_1'
matlab_data = load_matlab_data_file(directory, current_file_name) 

# Explore array values
m = matlab_data['hrf']
m[0][1] # 2nd index has the important values

# Load Python files
python_data = __import__(current_file_name)