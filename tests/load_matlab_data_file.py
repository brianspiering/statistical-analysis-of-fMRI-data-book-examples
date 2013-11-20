import os
import scipy.io

directory = os.getcwd() + '/matlab_data/'
file_name = 'box3_1'

def load_matlab_data_file(directory, filename):
    os.chdir(directory) # change to data dir
    return scipy.io.loadmat(file_name) # load data file