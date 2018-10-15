"""
super()
__mro__
"""


class A:
    name = "testName"

    def __init__(self):
        self.name = "classA"


class B(A):
    def __init__(self):
        self.name = super().name + "classB"


print(A.__mro__)
print(B.__mro__)
for v in B.__mro__:
    print(v, type(v), sep="///")

print(A.name)
print(A().name)
print(B.name)
print(B().name)
