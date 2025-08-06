import numpy as np

array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])

print("Array1:", array1)
print("Array2:", array2)
print("Common values between two arrays:")

for i in array1:
    if i in array2:
        print(i)
