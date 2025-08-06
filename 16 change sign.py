import numpy as np

array1 = np.arange(0, 20)

print("Original array:", array1)
for i in array1:
    if 9 <= i <= 15:
        print("You will change the sign of this number:", -i)
