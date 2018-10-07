# tuple
help(tuple)

# tuple.count tuple.index
tuple1 = (1, 2, 3, 1, 5)
print(tuple1)
print(tuple1.count(1))
print(tuple1.index(5))
try:
    print(tuple1.index(5, 0, 3))
except ValueError:
    print("You know what happened here...")
print("^" * 50)


# dict
help(dict)


# dict.clear
dict1 = {1: 'a', 2: 'b', 3: 'c'}
print(dict1)
dict1.clear()
print(dict1)

# dict.copy
dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = dict1.copy()
print(dict2)

# dict.fromkeys
list1 = [1, 2, 3, 4]
dict1 = {}.fromkeys(list1)
dict2 = {}.fromkeys(list1, 'a')
print(dict1, dict2, sep="\n")

# dict.get
print(dict2.get(3))
print(dict2.get(5))
print(dict2.get(5, 'default value'))

# dict.items
for k, v in dict2.items():
    print(k, v, sep=" --- ")
    print(type(k), type(v), sep=" *** ")

for kv in dict2.items():
    print(kv, type(kv), sep=" ^^^ ")

print(dict2.items())


print("*" * 50)

# dict.pop
print(dict1)
print(dict1.pop(3))
print(dict1)
print(dict1.pop(10, 'no value'))
print(dict1)

# dict.popitem
print(dict1.popitem())
print(dict1)

# dict.setdefault
dict1.setdefault(3, "Three")
dict1.setdefault(1, "One")
print(dict1)

# dict.update
dict1.update({1: "One"})
print(dict1)

print("&" * 50)


# set
set1 = set()
print(set1)

list1 = [1, 2, 3, 4, 9, 1, 3, 5, 4]
set1 = set(list1)
print(list1)
print(set1)

tuple1 = (1, 3, 5, 1, 'a', 'b', 'c')
print(type(tuple1), tuple1, sep=" **** ")

list2 = list(tuple1)
print(type(list2), list2, sep=" **** ")

set2 = set(tuple1)
print(type(set2), set2, sep=" **** ")

set2.add("abbbb")
print(set2)

# set.clear
# set.copy
# set.pop
print(set2.pop())
print(set2)
print(set2.pop())
print(set2)

# set.remove
# set.discard
# set.difference

