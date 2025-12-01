import numpy as np


def task1():
    print("Task 1  Create NumPy Arrays")
    arr1 = np.arange(1, 11)
    print("1D array:", arr1)

    arr2 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
    print("\n2D array:\n", arr2)
    print("Shape:", arr2.shape)
    print()


def task2():
    print("Task 2  Reshape Practice")
    arr = np.arange(12)
    reshaped_3x4 = arr.reshape(3, 4)
    reshaped_2x6 = arr.reshape(2, 6)

    print("Original:", arr)
    print("Reshaped to (3,4):\n", reshaped_3x4)
    print("Reshaped to (2,6):\n", reshaped_2x6)
    print("Note: reshape only changes the shape, not the data.\n")


def task3():
    print("Task 3  Axis Practice (mean, sum)")
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

    mean_axis0 = matrix.mean(axis=0)
    mean_axis1 = matrix.mean(axis=1)
    sum_axis0 = matrix.sum(axis=0)
    sum_axis1 = matrix.sum(axis=1)

    print("Matrix:\n", matrix)
    print("Mean axis=0 (column-wise):", mean_axis0)
    print("Mean axis=1 (row-wise):   ", mean_axis1)
    print("Sum axis=0 (column-wise):", sum_axis0)
    print("Sum axis=1 (row-wise):   ", sum_axis1)
    print("axis=0 -> down columns, axis=1 -> across rows.\n")


def task4():
    print("Task 4  Comparison Operations")
    arr = np.random.randint(0, 50, size=10)
    mean_val = arr.mean()
    greater_than_mean = arr[arr > mean_val]

    print("Array:", arr)
    print("Mean:", mean_val)
    print("Values > mean:", greater_than_mean)
    print()


def task5():
    print("Task 5  Masking and Filtering")
    arr = np.arange(21)

    even = arr[arr % 2 == 0]
    div3 = arr[arr % 3 == 0]

    print("Original:", arr)
    print("Even numbers:", even)
    print("Divisible by 3:", div3)
    print()


class MatrixTool:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def row_mean(self):
        """Return row-wise means."""
        return self.matrix.mean(axis=1)

    def above_threshold(self, t):
        """Return values greater than t."""
        return self.matrix[self.matrix > t]


def task6():
    print("Task 6  Small OOP + NumPy")
    example_matrix = [[1, 5, 10],
                      [3, 7, 2]]

    tool = MatrixTool(example_matrix)

    print("Matrix:\n", tool.matrix)
    print("Row-wise means:", tool.row_mean())
    print("Values > 4:", tool.above_threshold(4))
    print()


def task7():
    print("Task 7  Mini Challenge")
    mat = np.random.random((5, 5))
    result = np.where(mat < 0.5, 0, 1)

    print("Original matrix:\n", mat)
    print("\nThresholded matrix (0 if <0.5, 1 if >=0.5):\n", result)
    print()


def main():
    while True:
        print("1  Task 1: Create arrays")
        print("2  Task 2: Reshape practice")
        print("3  Task 3: Axis practice")
        print("4  Task 4: Comparison operations")
        print("5  Task 5: Masking and filtering")
        print("6  Task 6: OOP + NumPy")
        print("7  Task 7: Mini challenge")
        choice = input("Choose a task number: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "6":
            task6()
        elif choice == "7":
            task7()
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()