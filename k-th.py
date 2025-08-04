list1 = list(range(1, 10))  
k = int(input("Enter the value of k: "))

if k < 1 or k > len(list1):
    print("k is out of range.")
else:
    print(f"The {k}-th element in the list is: {list1[k - 1]}")
