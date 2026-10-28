import numpy as np

matrix_2d = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

print("Original 3x3 Matrix:")
print(matrix_2d)

array_1d = matrix_2d.reshape(9)

print("\nReshaped to 1D Array:")
print(array_1d)

matrix_back = array_1d.reshape(3, 3)

print("\nFlattened Back to 3x3 Matrix:")
print(matrix_back)