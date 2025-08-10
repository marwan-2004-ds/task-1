import numpy as np

array1 = np.array([0, 1, 3])
array2 = np.array([2, 4, 5])

print("Original array1:")
print(array1)

print("Original array2:")
print(array2)


result = np.corrcoef(array1, array2)

print("Pearson product-moment correlation coefficients of the said arrays:")
print(result)
