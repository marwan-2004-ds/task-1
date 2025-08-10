import numpy as np

array1 = np.array([[0 , 1], [2, 3]])

print("Maximum value of the above flattened array:", np.max(array1.flatten()))
print("Minimum value of the above flattened array:", np.min(array1.flatten()))