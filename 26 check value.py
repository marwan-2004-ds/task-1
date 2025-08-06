import numpy as np

array = np.array([[1.12, 2, 3.45], [2.33, 5.12, 6.0]])
print("Original array:")
print(array)

values_to_check = [1.12, 4, 5.12, 0, 6.0]

for value in values_to_check:
    print(value in array)
