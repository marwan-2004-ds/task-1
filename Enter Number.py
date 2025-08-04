number = 0 

while number >= 0:
    number = float(input("Enter a number (enter a negative number to exit): "))
    if number >= 0:
        print(f"You entered: {number}")

print("Negative number entered. Exiting the program.")
