import re

s = "Here is a simple string."

p = re.compile(r"([a-z]+) ([a-z]+)", re.I)

m = p.match(s)

print(m)

print(m.groups(), m.group(), m.group(0), m.group(1), m.group(2), sep="////")
print(m.start(0), m.start(1), m.start(2), sep="////")
print(m.end(0), m.end(1), m.end(2), sep="////")
