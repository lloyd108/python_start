import re


s1 = "This12is34a56simple78text."

p1 = re.compile(r"simple")
p2 = re.compile(r"^[A-Za-z]*")
p3 = re.compile(r"\d+")

m1 = p1.search(s1)
m2 = p2.match(s1)
m3 = p3.match(s1, 4, 20)
m4 = p3.findall(s1)

print(m1, m2, m3, sep="///")
print(m2.start(), m2.end(), m2.span(), sep="&&&")

print(m4)