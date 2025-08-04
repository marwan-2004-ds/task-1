num = int(input("Enter a number: "))
if num in range(0, 10):
    print("The number is in the specified range (0-9).")
elif num in range(10, 21):
    print("The number is in the specified range (10-20).")
elif num in range(21, 31):
    print("The number is in the specified range (21-30).")
elif num in range(31, 41):
    print("The number is in the specified range (31-40).")
else:
    print("The number is outside the specified ranges (0-40).")