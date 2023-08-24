my_list = [3, 6, 4, 2, 1, 5]
my_list.sort()
print(my_list)

my_list = ['Cabbage', 'Apple', 'Banana', 'Potato']
my_list.sort()
print(my_list)

my_list = ['This is a long sentence', 'Word', 'Z']

my_list.sort(key = len)
print(my_list)

my_list = ['This is a long sentence','Word', 'Z']
my_list.sort(key = len, reverse=True)
print(my_list)

my_list = [('John', 2), ('Steve', 2), ('Joe', 3)]

def sort_tuple(tuple_value):

    return tuple_value[1]

my_list.sort(key = sort_tuple)
print(my_list)

my_list = [3, 6, 4, 2, 1, 5]
sorted_list = sorted(my_list)
print(my_list)
print(sorted_list)

my_list = ['Loquacious', 'Chatty', 'Talkative']
sorted_list = sorted(my_list, key=len, reverse=True)
print(sorted_list)

my_list = [0, 1, 2, 3]
my_list[0] = None
print(my_list)

my_list = [0, 1, 2, 3]
my_list.append(4)
print(my_list)

my_list = ['a', 'b', 'c', 'd', 'f']
my_list.insert(4, 'e')
print(my_list)
my_list.insert(1000, 'g')
print(my_list)

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del(my_list[0])
print(my_list)
del(my_list[0:3])
print(my_list)

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_list.pop()
my_list.pop(0)
my_list.remove('f')
print(my_list)
my_list.clear()
print(my_list)

for n in range (4):
    print(n)

my_list = [0, 1, 2, 3] 
print(my_list)

my_range = range(4)
print(my_range)

my_string = 'Hello world!'
for char in my_string:
    print(char)

my_string = 'hello world!'
my_string.upper()
print(my_string)    