def multi_agrs(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(multi_agrs(20, 30, 40, 10))

#**************************#
def p_dict(**args):
    for arg in args:
        print("{0}:{1}".format(arg, args[arg]))
p_dict(a=2, b=3, c=4)
    
#**************************#

def all_print(a, *args, **largs):
    print(a)
    print(args)
    print(largs)
all_print(10, 20, 30, c=3, b=4, d=5)      
