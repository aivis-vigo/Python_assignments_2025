# numpy_utils.py
# All NumPy helper functions and classes
# Author: Yangli Deng

import numpy as np

# Task 1
def create_arrays():
    """Create a 1D and 2D NumPy array"""
    arr1d = np.arange(1, 11)
    arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
    return arr1d, arr2d

# Task 2
def reshape_array(arr):
    """Reshape array into (3,4) and (2,6)"""
    reshaped_3x4 = arr.reshape(3,4)
    reshaped_2x6 = arr.reshape(2,6)
    return reshaped_3x4, reshaped_2x6

# Task 3
def axis_operations(matrix):
    """Compute mean along axis=0 and sum along axis=1"""
    mean_axis0 = matrix.mean(axis=0)
    sum_axis1 = matrix.sum(axis=1)
    return mean_axis0, sum_axis1

# Task 4
def values_greater_than_mean(arr):
    """Return values greater than the mean"""
    mean_val = arr.mean()
    filtered = arr[arr > mean_val]
    return filtered, mean_val

# Task 5
def mask_even_div3(arr):
    """Return even numbers and numbers divisible by 3"""
    even_numbers = arr[arr % 2 == 0]
    div3_numbers = arr[arr % 3 == 0]
    return even_numbers, div3_numbers

# Task 6
class MatrixTool:
    """Class for row-wise mean and threshold filtering"""
    def __init__(self, array):
        self.array = np.array(array)
    
    def row_mean(self):
        return self.array.mean(axis=1)
    
    def above_threshold(self, t):
        return self.array[self.array > t]

# Task 7
def threshold_matrix(matrix):
    """Replace values <0.5 with 0, >=0.5 with 1"""
    return np.where(matrix < 0.5, 0, 1)
