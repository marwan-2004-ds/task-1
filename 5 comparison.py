import numpy as np

array1 = np.array([1, 2, 0, 4, 0, 6])
array2 = np.array([3, 2, 0, 1, 0, 5])

for i in array1:
    for j in array2:
        if i > j:
            print(f"{i} > {j}")
        elif i < j:
            print(f"{i} < {j}")
        elif i >= j:
            print(f"{i} >= {j}")
        else:
            print(f"{i} <= {j}")
