matrix_1d = []#is blank
matrix_2d = [[1, 2, 3], [4, 5, 6]]#is a 2D array

for row in matrix_2d:
    for num in row:
        matrix_1d.append(num)
print(matrix_1d) #2 array will convert into one variable

print("-------------------------------")
print("By using list comprehension")
#By using comprehension

matrix_1d = [num for row in matrix_2d for num in row]
print(matrix_1d)


#If you want to squre every value in variable
print("-------------------------------")
print("Squre all value in variable")

matrix_1d = [num**2 for row in matrix_2d for num in row]
print(matrix_1d)
