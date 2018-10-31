import sys
import os


print(os.getcwd())
print(os.listdir())

with open('base.txt', 'r', encoding='utf-8', errors='ignore') as f:
    print(type(f))
    line = f.readline(30)
    content = f.readlines()

print(type(content))
print(type(line))

with open('archer', 'w', encoding='utf-8') as a:
    for v in content:
        a.write(v)

with open('archer_line', 'a', encoding='utf-8') as b:
    b.write(line)

print(content)
print(line)
