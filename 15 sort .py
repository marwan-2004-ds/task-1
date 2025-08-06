import numpy as np

array = np.array([[4, 6], [2, 1]])

print("Original array:")
print(array)

print("\nSort along the first axis:")
print(np.sort(array, axis=0))

print("\nSort along the last axis:")
print(np.sort(array, axis=1))
