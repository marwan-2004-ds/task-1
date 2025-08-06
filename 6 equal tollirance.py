import numpy as np

arr1 = [1.0, 2.0, 3.0, 5, 6]
arr2 = [1.0, 2.00000001, 2.99999999, 5, 6]

for i in range(len(arr1)):
    a = arr1[i]
    b = arr2[i]

    if a == b:
        print(f"{a} is  equal to {b}")
    elif np.isclose(a, b):
        print(f"{a} is close to {b} (within tolerance)")
    else:
        print(f"{a} is not equal to {b}")
