num1 = int(input("Enter The 1st Number: "))
num2 = int(input("Enter The 2nd Number: "))
num3 = int(input("Enter The 3rd Number: "))

if num1 > num2 and num1 > num3:
    print("num1 is the greatest number")
elif num2 > num1 and num2 > num3:
    print("num2 is the greatest number")
elif num3 > num1 and num3 > num2:
    print("num3 is the greatest number")
else:
    print("There is a tie between the greatest numbers")
