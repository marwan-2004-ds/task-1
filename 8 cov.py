import numpy as np

# Original arrays
array1 = np.array([0, 1, 3])
array2 = np.array([2, 4, 5])

print("Original array1:")
print(array1)

print("Original array2:")
print(array2)

# Compute cross-correlation
result = np.correlate(array1, array2)

print("Cross-correlation of the said arrays:")
print(result)
