import numpy as np

'''Task 1'''
# 1D array from 1 to 10
arr1 = np.arange(1, 11)

# 2D array 3x3
arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

print("Task 1:")
print("1D array:", arr1)
print("2D array:\n", arr2)
print("Shape of 2D array:", arr2.shape)
print()


'''Task 2'''
'''
Explain why reshape does not change array data: Because reshape does not change the actual data in array, 
It only changes the view of how data is interpretated, so elements remain same, even if the array looks quite different.
'''
arr12 = np.arange(12)

reshaped_3x4 = arr12.reshape(3, 4)
reshaped_2x6 = arr12.reshape(2, 6)

print("Task 2:")
print("Reshaped to (3,4):")
print(reshaped_3x4)
print()

print("Reshaped to (2,6):")
print(reshaped_2x6)
print()


'''Task 3'''
'''
Explain what each axis means: 
axis=0 means the operation applies down each column
axis=1 means the operation applies across each row
'''
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

mean_axis0 = np.mean(matrix, axis=0)
sum_axis1 = np.sum(matrix, axis=1)

print("Task 3:")
print("Matrix:\n", matrix)
print("Mean along axis=0:", mean_axis0)
print("Sum along axis=1:", sum_axis1)
print()


'''Task 4'''
# Created array with 10 random integers
rand_arr = np.random.randint(0, 50, 10)

mean_val = rand_arr.mean()

greater_than_mean = rand_arr[rand_arr > mean_val]

print("Task 4:")
print("Random array:", rand_arr)
print("Mean:", mean_val)
print("Values > mean:", greater_than_mean)
print()


'''Task 5'''
arr = np.arange(0, 21)

# Boolean mask for even numbers
even_numbers = arr[arr % 2 == 0]

# Boolean mask for numbers divisible by 3
div_by_3 = arr[arr % 3 == 0]

print("Task 5:")
print("Array 0–20:", arr)
print("Even numbers:", even_numbers)
print("Numbers divisible by 3:", div_by_3)
print()


'''Task 6'''
class MatrixTool:
    def __init__(self, matrix):
        self.matrix = matrix

    def row_mean(self):
        # row-wise means
        return np.mean(self.matrix, axis=1)

    def above_threshold(self, t):
        # values > t
        return self.matrix[self.matrix > t]


# Example usage:
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

tool = MatrixTool(matrix)

print("Task 6:")
print("Row means:", tool.row_mean())
print("Values above threshold 5:", tool.above_threshold(5))


'''Task 7 mini challenge'''
# Generate a 5x5 random matrix (values from 0 to 1)
matrix = np.random.rand(5, 5)

# Thresholding using masks
binary_matrix = np.where(matrix < 0.5, 0, 1)

print("Task 7:")
print("Original matrix:\n", matrix)
print("\nBinary matrix (thresholded):\n", binary_matrix)
print()
