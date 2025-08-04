list1 = input("Enter a list of numbers separated by commas: ")
list1 = [int(x) for x in list1.split(',')]
print("You entered the list:", list1)

list2 = list(set(list1))  
print("Unique elements in the list:", list2)
