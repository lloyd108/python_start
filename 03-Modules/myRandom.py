import random
import logging

num = random.random()
print(num)

print(int(num * 100))
print(int(num * 100 // 1))

list1 = ["choice" + str(i) for i in range(10)]
print(list1)
print(random.choice(list1))

list2 = list1
random.shuffle(list2)
print(list1)

print(random.randint(10, 20))
print(random.randrange(10, 20))
