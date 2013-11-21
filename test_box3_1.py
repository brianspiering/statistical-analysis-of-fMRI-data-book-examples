# Test Box 3_1.py

# TODO:  Learn TDD
# Refactor to generalize to all files

import unittest, os
import scipy.io

def load_matlab_data_file(directory, filename):
    return scipy.io.loadmat(directory + filename) # load MATLAB file into dict

class TestBoxAll(unittest.TestCase):
  
    # Test hrf function values
    def test_hrf(self):
        name = 'box3_1'
        
        # Load MATLAB data, aka the ground truth
        directory = os.getcwd()  + '/matlab_files/'
        matlab_data = load_matlab_data_file(directory, name) 
        
        # Load Python data
        python_data = __import__(name)
        
        self.assertEqual(matlab_data['hrf'], python_data.hrf)
       
    # TODO: Test all dict keys

if __name__== "__main__":
    unittest.main()
    
# TODO: move tests to separate folder