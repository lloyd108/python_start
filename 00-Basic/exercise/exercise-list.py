help(list)

print("*" * 50)

# list.append
l1 = [1, 2, 3, 4, 5]
print(id(l1))
l1.append((5, 6, 7))
print(id(l1))
print(l1)

# list.copy
l2 = l1.copy()
print(id(l1), id(l2), sep="\n")
print(l2)
for v in l2:
    print(v)

# list.count
print(l2.count(1))

# list.extend  i.e. list + list
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = l1 + l2
print(l3)
print(id(l1))
print(l1.extend(l2))
print(id(l1))
help(list.extend)

print("#" * 30)
# list.index
list1 = [1, 2, 3, 1, 3, 1, 2, 3, 4, 6]
try:
    print(list1.index(6))
    print(list1.index(6, 0, 5))
except ValueError:
    print("value error")
help(list.index)

print("*" * 30)

# list.insert
list1 = [1, 2, 3, 4, 5, 'a', 'b']
list1.insert(1, 'c')
print(list1)


# list.pop
v1 = list1.pop(len(list1) - 1)
v2 = list1.pop(0)
v3 = list1.pop()
print(list1, v1, v2, v3, sep=" && ")

print("*" * 30)

# list.remove
print(list1)
list1.remove('c')
print(list1)
try:
    list1.remove('a')
except ValueError:
    print("some error occurs, guess what is it?")

# list.reverse
list1 = [1, 5, 4, 2, 3, 'd', 'b', 'a', 'c']
print(list1)
print(id(list1))
list1.reverse()
print(list1)
print(id(list1))

print("&" * 50)
# list.sort
list1 = [1, 5, 4, 2, 3]
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
help(list.reverse)