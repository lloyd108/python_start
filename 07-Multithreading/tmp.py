class People:
    def __init__(self, num):
        print("I'm people {0}!".format(num))
        self.num = num

    def say(self):
        return self.num


for i in range(10):
    p = People(i)

print(p.say())