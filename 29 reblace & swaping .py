import numpy as np

array1 = np.array([
    [1, 2, 0, 6],
    [4, 0, 6, 10],
    [0, 0, 0, 0],
    [6, 6, 6, 6]
])

print(array1)

first = array1[0, 0]
second_col = array1[:, 1]
third_col = array1[:, 2]
last = array1[-1, -1]

array1[:, 2] = second_col
array1[:, 1] = third_col
array1[0, 0] = last
array1[-1, -1] = first

print(array1)
