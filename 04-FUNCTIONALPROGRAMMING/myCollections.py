import collections

Point = collections.namedtuple("Point", ['x', 'y'])
p = Point("abc", 15)
print(p.x, p.y, sep="///")


Circle = collections.namedtuple("Circle",['x', 'y', 'z'])
c = Circle(100, 100, 50)

print(type(c))
print(c)

q = collections.deque(['a', 'b', 'c'])
print(q)

q.append("d")
print(q)

q.appendleft('x')
print(q)

s1 = 'asdfasdfasdfasdfasdqwefavbzxcbasdf'
c1 = collections.Counter(s1)
print(c1)