my_list = list(range(1,11))

count = 0
for x in my_list:
    if x % 2 == 0:
        count += 1
        print('total even NUM are : ' , count )