def find_largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest = find_largest(a, b)
print("The largest number is:", largest)
