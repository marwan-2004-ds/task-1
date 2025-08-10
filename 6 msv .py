import numpy as np

arr = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11]])

print("Original array:")
print(arr)

mean_val = np.mean(arr, axis=1)
std_val = np.std(arr, axis=1)
var_val = np.var(arr, axis=1)

print("Mean:", mean_val)
print("std:", std_val)
print("variance:", var_val)
