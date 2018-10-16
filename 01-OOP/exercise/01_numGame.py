import random

"""
输入一个三位数与程序随机数比较大小
1. 如果大于程序随机数,则分别输出这个三位数的个位\十位\百位
2. 如果等于程序随机数,则提示中奖,记100分
3. 如果小于程序随机数,则将120个字符输入到文本文件中
    (规则是每一条字符串的长度为12,单独占一行,并且前四个是字母,后8个是数字)
"""


class NumGame():
    score = 0
    cnt = 0

    # 1. 输入数字, exit退出
    def inputnum(self):
        value = input("请输入三位数字(100~999):")
        if value.isdigit() and 99 < int(value) < 1000:
            return int(value)
        elif value.lower() == "exit":
            print("您总共玩了{0}局, 总分为{1}".format(self.cnt, self.score))
            exit()
        else:
            print("输入错误,请...")
            return 0

    # 2. 生成随机数
    @staticmethod
    def genrandom():
        value = random.randrange(100, 1000)
        return value

    # 3. 比较大小
    def numcmp(self, num, rdm):
        if num != 0:
            print("输入的数字为{0}, 随机生成的数字为{1}...".format(num, rdm))
            if num > rdm:
                self.numout(num)
            elif num == rdm:
                self.addscore()
            else:
                self.writefile()
            self.cnt += 1

    # 3.1 输出三位数的个位/十位/百位
    @staticmethod
    def numout(num):
        bai = num // 100
        shi = num % 100 // 10
        ge = num % 10
        print("输入数字的百位为{0}、十位为{1}、个位为{2}...".format(bai, shi, ge))

    # 3.2 提示中奖, 记100分
    def addscore(self):
        print("您已中奖, 得到100分...")
        self.score += 100

    # 3.3 生成随机字符, 写入文件
    @staticmethod
    def genline():
        line_str = ""

        for _ in range(4):
            line_str += chr(random.randrange(97, 123))

        for _ in range(8):
            line_str += str(random.randrange(0, 10))

        return line_str

    def writefile(self):
        with open("numGame.txt", "a", encoding="utf-8") as f:
            f.write("第{0}局, 总分为{1}...\n".format(self.cnt, self.score))
        for _ in range(10):
            with open("numGame.txt", "a") as f:
                f.write(self.genline() + "\n")
        print("文件已写入.")

    def startgame(self):
        self.score = 0
        self.cnt = 0

        while True:
            self.numcmp(self.inputnum(), self.genrandom())
            # self.numcmp(self.inputnum(), 778)

            print("您玩的这是第{0}局, 积分为{1}...".format(self.cnt, self.score))


if __name__ == "__main__":
    game1 = NumGame()
    game1.startgame()
