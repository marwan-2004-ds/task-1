import numpy as np

arr = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11]])

print("Original array:")
print(arr)

diff = np.max(arr ,axis=1) - np.min(arr , axis=1)

print("Difference between the maximum and the minimum values of the said array:")
print(diff)
