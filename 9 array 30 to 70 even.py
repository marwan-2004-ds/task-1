import numpy as np

arrray = np.array([np.arange(30, 71)])

for i in arrray[0]:
    if i % 2 == 0:
        print(i)
    else:
        print("Found an odd number:", i)