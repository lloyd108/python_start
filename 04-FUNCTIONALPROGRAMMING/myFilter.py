l1 = [i for i in range(100)]

f1 = filter(lambda x: x % 5 == 0, l1)
print(l1, type(f1), f1, sep='\n')

l2 = [i for i in f1]
print(l2)

for i in range(-100, -60):
    l2.append(i)

l3 = sorted(l2, reverse=True)
l4 = sorted(l3, reverse=True, key=abs)
l2.pop()
l2.remove(10)
print(l2, l3, l4, sep='\n')