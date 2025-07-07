def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    else :
        return a / b

a = int(input(' enter the first num :')) 
b = int(input(' enter the second num :'))
operation = input('Enter the operation (+, -, *, /): ')

result = calculator(a, b, operation)
print("Result:", result)
