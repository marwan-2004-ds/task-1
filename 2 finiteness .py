import numpy as np

array = np.array([5, -10, -6, 0, 1, -1])
array2 = np.array([5, -20, -12, 0, 0, 0])

result = np.divide(array, array2)

for i in result:
    if np.isfinite(i):
        print(f"{i} is finite")
    elif np.isinf(i):
        print(f"{i} is infinite")
    else:
        print(f"{i} is NaN (Not a Number)")
