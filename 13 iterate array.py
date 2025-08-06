import numpy as np

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("3x4 Array:")
print(array)

print("\nIterating  elements:")
for row in array:
    for element in row:
        print(element, end=' ')
