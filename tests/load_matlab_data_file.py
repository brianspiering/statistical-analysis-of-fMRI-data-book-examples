import os, sys
import scipy.io

file_name = 'box3_1.mat'

def load_matlab_data_file(filename):
    os.chdir(os.path.dirname(sys.argv[0])+'/matlab_data/') # change to data dir
    return mat = scipy.io.loadmat(file_name) # load in data file