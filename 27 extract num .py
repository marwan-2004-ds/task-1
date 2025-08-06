import numpy as np

array1 = np.array([1, 2, 0, 4, 0, 6 , 10])
checked_numbers = int(input("Enter a number to check: "))

for i in array1:
    if i > checked_numbers:
        print(f"{i} is greater than {checked_numbers}")
    elif i == checked_numbers:
        print(f"{i} is equal to {checked_numbers}")
    else:
        print(f"{i} is less than {checked_numbers}")