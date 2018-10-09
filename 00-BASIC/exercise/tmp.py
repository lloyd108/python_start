def my_while(c):
    a = 0
    while True:
        a += 1
        if a == 99:
            print(a, c)
            break


c = input("Please input something here:")

my_while(c)

