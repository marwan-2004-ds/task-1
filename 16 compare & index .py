import numpy as np

array = np.array([[0, 10, 20], [20, 30, 40]])

print("Values bigger than 10 and their indices:")

for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        if array[i][j] > 10:
            print(f"Value: {array[i][j]} at index ({i}, {j})")
