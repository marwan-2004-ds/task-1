my_list = list(range(1, 50))

num = int(input('Enter the number you want to search for: '))

if num in my_list:
    index = my_list.index(num)
    print('The number is found at index:', index)
else:
    print('The number is not found in the list.')
