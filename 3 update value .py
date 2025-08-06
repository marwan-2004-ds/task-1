import numpy as np

array1 = np.zeros(10)

print("Array filled with zeros:")
print(array1)

for i in range(len(array1)):
    if i == array1[6]:
        array1[6] = 11
        print("Updated value at index 6 to 11" , array1)