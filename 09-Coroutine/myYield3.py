def gen():
    for i in "abc":
        yield i


print(list(gen()))


def gen_new():
    yield from "abc"


print(list(gen_new()))


for v in gen():
    print(v)


for v in gen_new():
    print(v)