# assignment5.py
# Main script to run NumPy homework
# Author: Yangli Deng

import numpy as np
from numpy_utils import *

def main():
    print("=== NumPy Homework Script Running ===\n")

    # Task 1
    arr1d, arr2d = create_arrays()
    print("Task 1 - 1D array:", arr1d)
    print("Task 1 - 2D array:\n", arr2d)

    # Task 2
    arr12 = np.arange(1,13)
    reshaped_3x4, reshaped_2x6 = reshape_array(arr12)
    print("\nTask 2 - Reshaped to 3x4:\n", reshaped_3x4)
    print("Task 2 - Reshaped to 2x6:\n", reshaped_2x6)

    # Task 3
    matrix3x3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    mean_axis0, sum_axis1 = axis_operations(matrix3x3)
    print("\nTask 3 - 3x3 matrix:\n", matrix3x3)
    print("Mean along axis 0 (columns):", mean_axis0)
    print("Sum along axis 1 (rows):", sum_axis1)

    # Task 4
    rand_arr = np.random.randint(0, 20, size=10)
    filtered, mean_val = values_greater_than_mean(rand_arr)
    print("\nTask 4 - Random array:", rand_arr)
    print("Mean value:", mean_val)
    print("Values greater than mean:", filtered)

    # Task 5
    arr0_20 = np.arange(0,21)
    even_numbers, div3_numbers = mask_even_div3(arr0_20)
    print("\nTask 5 - Even numbers:", even_numbers)
    print("Numbers divisible by 3:", div3_numbers)

    # Task 6
    tool = MatrixTool([[1,2,3],[4,5,6],[7,8,9]])
    print("\nTask 6 - Row-wise mean:", tool.row_mean())
    print("Values above 5:", tool.above_threshold(5))

    # Task 7
    rand5x5 = np.random.rand(5,5)
    print("\nTask 7 - Random 5x5 matrix:\n", rand5x5)
    thresholded = threshold_matrix(rand5x5)
    print("Thresholded 5x5 matrix:\n", thresholded)

    print("\n=== Script Finished ===")

if __name__ == "__main__":
    main()
