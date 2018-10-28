l1 = [i for i in range(10)]
print(l1)

l2 = []

for _ in l1:
    l2.append(_ * 10)
print(l2)

l3 = map(lambda x: x * 11, l1)
print(l3)
for i in l3:
    print(i)

l4 = [i for i in l3]
print(l4)
