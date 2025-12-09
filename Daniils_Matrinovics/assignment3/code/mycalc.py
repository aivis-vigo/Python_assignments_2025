import numpy as np

def magic(num_list):
    num_arr = np.array(num_list)
    dot_product = np.dot(num_arr, num_arr)
    max_value = np.max(num_arr)
    return dot_product * max_value