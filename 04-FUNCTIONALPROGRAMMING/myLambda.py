def printa(value="AAAAA"):
    print(value)


tri_number = lambda x, y, z: z * 100 + y * 10 + x
my_print = lambda x = "xyz": print(x)

printb = printa


def get_info(obj):
    print(id(obj))
    print(type(obj))
    print(obj)



if __name__ == "__main__":
    printa()
    printa("BBBB")
    print(tri_number(7, 8, 9))
    my_print()
    my_print("abc")
    printb()
    get_info(printb)