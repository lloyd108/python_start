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

# 利用for循环
print("for loop1:")
for i in range(0, 4):
    print("* " * 5)

print("for loop2:")
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
print("for loop3:")
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
print("for loop4:")
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
for row in range(5):
    for col in range(row + 1):
        if row == 2 and col == 1:
            print("  ", end="")
        elif row == 3 and col in (1, 2):
            print("  ", end="")
        else:
            print("* ", end="")
    print()
