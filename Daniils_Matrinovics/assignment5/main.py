import numpy as np

# Task 1 – Create NumPy Arrays
# Create a 1D array of numbers from 1 to 10.
# Create a 2D array with shape (3,3).
# Print the array and its shape.
print("Task 1")

arr_1d = np.arange(1,11)
print(arr_1d)

arr_2d = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(arr_2d,arr_2d.shape)

# Task 2 – Reshape Practice
# Given an array of 12 elements, reshape it to (3,4).
# Then reshape it to (2,6).
# Explain why reshape does not change array data.
print("Task 2")

given_arr = np.arange(1,13)
reshaped_arr = np.reshape(given_arr,(3,4))
print(reshaped_arr)

reshaped_arr = np.reshape(given_arr,(2,6))
print(reshaped_arr)
# Reshape is only used to rearange data, it's not supposed to change any values only their arrangament in certain number of rows and columns

# Task 3 – Axis Practice (mean, sum)
# Create a 3x3 matrix.
# Compute mean along axis=0.
# Compute sum along axis=1.
# Explain what each axis means.
print("Task 3")

matrix = np.arange(1,10).reshape(3,3)

#axis=2 means that a calculation happen column by column
mean = np.mean(matrix,axis=0)

#axis=1 means that a calculation happen row by row
sum = np.sum(matrix,axis=1)

print(matrix, mean, sum)

# Task 4 – Comparison Operations
# Create an array of 10 random integers.
# Find values greater than the mean.
# Return them as a new array.
print("Task 4")

random_arr = np.random.randint(10,size=10)
print(random_arr)

mean = np.mean(random_arr)
print(mean)

above_mean_mask = random_arr > mean
print(random_arr[above_mean_mask])

# Task 5 – Masking and Filtering
# Create an array 0–20.
# Extract even numbers using a Boolean mask.
# Extract numbers divisible by 3.
print("Task 5")

arr20 = np.arange(21)
print(arr20)

even_mask = [x%2==0 for x in arr20]
print(even_mask)
print(arr20[even_mask])

# Task 6 – Small OOP + NumPy
# Write class MatrixTool:
# method row_mean() → row-wise means
# method above_threshold(t) → values > t
# Use NumPy arrays as input.
print("Task 6")

class MatrixTool:
    def row_mean(np_arr):
        return np.mean(np_arr, axis=1)
    def above_threshold(np_arr, t):
        return np_arr[np_arr > t]

example_matrix = np.arange(1,13).reshape(3,4)
print(example_matrix)

print(MatrixTool.row_mean(example_matrix))
print(MatrixTool.above_threshold(example_matrix, 7))

# Task 7 – Mini Challenge
# Generate a 5x5 random matrix.
# Replace values < 0.5 with 0.
# Replace values ≥ 0.5 with 1.
# Learn thresholding + masking.
print("Task 7")

random_matrix = np.reshape(np.random.randint(100,size=25)/100, (5,5))
print(random_matrix)

# Thresholding
mask = random_matrix >= 0.5
print(mask)

# Masking
print(np.where(mask,1,0))