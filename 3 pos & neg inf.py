import numpy as np

array = np.array([ 5, -10, -6, 0, 1 , -1])
array2 = np.array([5, -20, -12, 0, 0, 0])

result = np.divide(array, array2)

for i in result:
    if np.isposinf(i):
        print(f"{i} is positive infinity")
    elif np.isneginf(i):
        print(f"{i} is negative infinity")
    else:
        print(f"{i} is neither positive nor negative infinity")
