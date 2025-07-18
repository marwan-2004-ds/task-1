import numpy as np

a = np.array ([10, 20, 30, 40, 50])
b = np.array ([5, 4, 3, 2, 1])

print("==========================")
print("== ARITHMATIC OPERATION ==" )
print("==========================")

print( a + b )
print( a - b )
print( a * b )
print( a / b )

print("==========================")


def find_mmm(a):
    word = input("Your choice (max / min / mean): ")

    if word == "max":
        print("Maximum:", np.max(a))
    elif word == "min":
        print("Minimum:", np.min(a))
    elif word == "mean":
        print("Mean:", np.mean(a))
    else:
        print("Invalid input. Please type 'max', 'min', or 'mean'.")


def dot_product(a, b):
    result = np.dot(a, b)
    print("Dot Product:", result)


def reshapee(a):
    reshaped = np.reshape(a, (5, 1))
    print("Reshaped array:\n", reshaped)

find_mmm(a)
dot_product(a , b)
reshapee(a)