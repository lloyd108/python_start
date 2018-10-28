import sys
import os


print(os.getcwd())
print(os.listdir())

with open('archer', 'r', encoding='utf-8') as f:
    print(type(f))
    # l1 = [i for i in f]
    content = f.readlines()

print(type(content))
for v in content:
    print(v)
print(list(content))
# print(l1)
