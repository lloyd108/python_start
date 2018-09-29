"""
exercise of string operations
"""

s1 = "This is str1."
s2 = "This is str2."
s3 = s1 + s2
print(s3)
print(s1 + " " + s2)
print(s1, s2, sep=" ")

s = "This is a string."
print(len(s1))
s1 = s * 5
print(s1)

for i in s:
    print(i)

print(s[0], s[1], s[2], s[3], s[-1], sep='/')
print(s[1:5])
print(s[s.__len__() - 1])
print(s[s.__len__():0:-1])
print(s[::-1])
print(s.__len__())
print(len(s))

print(id(s))
print(id(s[:]))
print(id(s[1:3]))

print("##########################")
print("\n\n\n\n\n\n\n\n")

s1 = "This is a new str."
s2 = s1
print(s1, s2, sep="=.= ")

l1 = list(s1)
l2 = l1
l2[3] = 'A'
print(l1[3])

help(str)
print("====================")
help(str.find)

print("#" * 30)
S = "THIS IS A SIMPLE STRING WITH UPPERCASE."
print(S.capitalize())
print(S.title())

s = "this is a simple string with lowercase."
print(s.upper())
print(S.swapcase(), s.swapcase(), sep="\n")
print(len(s), len(S), s.__sizeof__(), sep="###")

print(type(s.find("is")))
print(s.find("is"))

print(s.count('i'))
print(s.startswith('T'), S.startswith('T'), sep="////")
print(s.endswith('.'))
print(s.isupper(), S.isupper(), sep="//////")
print(s.islower(), S.islower(), sep="//////")
print(s.istitle(), S.istitle(), sep="//////")


print(s.split(" "))
print("*".join(S.split(" ")))