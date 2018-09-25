'''
exercise of for loop
'''

# print simple graphs

"""
* * * * *
* * * * *
* * * * *
* * * * *
"""
print("* * * * * \n" * 4)

print("* " * 5)
print("* " * 5)
print("* " * 5)
print("* " * 5)

# use for-loop:
print("for-loop1:")
for i in range(0, 4):
    print("* " * 5)

print("for-loop2:")
for i in range(0, 4):
    for j in range(0, 5):
        print("*", end=" ")
    print("\n", end="")

"""
* * * * *
*       *
*       *
* * * * *
"""
print("for-loop3:")
for line in range(0, 4):
    for row in range(0, 5):
        if line in (0, 3) or row in (0, 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
*
* *
* * *
* * * *
* * * * *
"""
print("for-loop4:")
for row in range(0,5):
    print("* " * (row + 1), end=" ")
    print("\n", end="")

"""
*
* *
*   *
*     *
* * * * *
"""
print("for loop5:")
side = 5
for row in range(side):
    for col in range(row + 1):
        if row in (0, side - 1) and col in (0, row):
            print("* ", end="")
    print()

"""
* * * * *
* * * *
* * *
* *
*
"""
print("for-loop6:")
for i in range(5, 0, -1):
    print("* " * i, end="")
    print()

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print("* ", end="")
    print()

"""
* * * * *
*     *
*   *
* *
*
"""
print("for-loop7:")
side = 5
for i in range(side, 0, -1):
    for j in range(i, 0, -1):
        if i in (side, 1) or j in (i, 1):
            print("* ", end="")
        else:
            print("  ", end="")
    print()

"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
print("for-loop8:")
