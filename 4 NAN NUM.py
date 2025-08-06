import numpy as np

array1 = np.array([1, 2, 0, 4, 0, 6])
array2 = np.array([3, 2, 0, 1, 0, 5])

result = np.divide(array1, array2)

for i in result:
    if np.isnan(i):
        print(f"{i} is NaN (Not a Number)")
    else:
        print(f"{i} is a valid number")