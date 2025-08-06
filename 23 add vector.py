import numpy as np


Matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
vector = np.array([10, 20 ,30])

result = Matrix + vector

print("Result of adding vector to each row of the matrix:")
print(result)