import numpy as np

array1 = np.array([1, 2, 0, 4, 0, 6 , 10])

for i in array1:
    if i != 0:
        print(i)
    else:
        print("Found a zero")