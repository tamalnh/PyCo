def multi_agrs(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(multi_agrs(20, 30, 40, 10))
