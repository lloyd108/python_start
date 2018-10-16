def numout(num):
    bai = num // 100
    shi = num % 100 // 10
    ge = num % 10
    print("输入数字的百位为{0}、十位为{1}、个位为{2}...".format(bai, shi, ge))

numout(789)