# Test Box 3_1.py

# TODO:  Learn TDD
# Refactor to generalize to all files

import unittest, os
import scipy.io

def load_matlab_data_file(directory, filename):
    os.chdir(directory) # change to data dir
    return scipy.io.loadmat(file_name) # load data file

# Load MATLAB data, aka the ground truth
directory = os.getcwd()  + '/matlab_data/'
file_name = 'box3_1'
current_mat = load_matlab_data_file(directory, file_name) 


class test_box3_1(unittest.TestCase):
  
    # Test 1st dict key
    def test_hrf(self):
       assertEqual(current_mat['hrf'], box3_1.hrf)
       
    # TODO: Test all dict keys

if __name__== "__main__":
    unittest.main()
    
# TODO: move tests to separate folder