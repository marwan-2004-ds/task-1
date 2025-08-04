numbers = int(input("Enter the range of numbers: "))

squares = {}

for i in range(1, numbers + 1):
    squares[i] = i ** 2

print("Dictionary of numbers and their squares:")
print(squares)
