import numpy as np

array1 = np.array([[0, 1], [2, 3]])

print("Maximum value along the second axis:", np.max(array1, axis=1))
print("Minimum value along the second axis:", np.min(array1, axis=1))