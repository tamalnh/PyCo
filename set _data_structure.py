#basic way
besic_way="""
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for value in my_list:
    if my_list.count(value) >1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

"""
print(besic_way)
#***************************

doc = """
set is a really useful data structure.
sets behave mostly like lists with the distinction that they can not contain duplicate values.
It is really useful in a lot of cases. For instance you might want to check whether there are duplicates in a list or not. You have two options.
The ﬁrst one involves using a for loop. Something like this:
"""
print(doc)


my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in my_list if my_list.count(x)>1])
print(duplicates)

#Sets also have a few other methods. Below are some of them.
#1
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
user_input=set(['red', 'brown'])
print(user_input.intersection(valid))

#2
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
user_input=set(['red', 'brown'])
print(user_input.difference(valid))
