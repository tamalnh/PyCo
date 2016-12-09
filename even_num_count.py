num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

even_num_list = []#blank

for num in num_list:
    if num % 2 == 0:
        even_num_list.append(num)
        print(even_num_list)
        

#Alternative way

even_num_list=[num for num in num_list if num % 2 == 0]
print (even_num_list)
