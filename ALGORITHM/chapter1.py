"""
basic algorithm
"""
import datetime

"""
sequence1:
-1,1,-1,1,-1,...,(-1)**n
"""

# algorithm 1-1
def seq1_1():
    n = input("Please input power of n for 1-1:")
    starttime = datetime.datetime.now()
    if n.isdigit():
        if int(n) % 2 == 0:
            endtime = datetime.datetime.now()
            print("runction1 runs {0} microsecond.".format((starttime - endtime).microseconds))
            return 0
        else:
            endtime = datetime.datetime.now()
            print("function1 runs {} microsecond.".format((starttime - endtime).microseconds))
            return -1
    else:
        print("Input error.")
        return -99


# algorithm 1-2
def seq1_2():
    v_sum = 0
    n = input("Please input power of n for 1-2:")
    starttime = datetime.datetime.now()
    if n.isdigit():
        for v in range(1, int(n) + 1):
            v_sum += (-1) ** v
        endtime = datetime.datetime.now()
        print("function2 runs {} microsecond.".format((starttime - endtime).microseconds))
        return v_sum
    else:
        print("Input error.")
        return -99


"""
sequence2:
1, 2, 3, 4, 5, ...., n
"""


def seq2_1(n):
    sum = 0
    starttime = datetime.datetime.now()
    for i in range(1, n + 1):
        sum += i
    endtime = datetime.datetime.now()
    print("function3 runs {} microsecond.".format((starttime - endtime).microseconds))
    return sum


def seq2_2(n):
    starttime = datetime.datetime.now()
    sum = (1 + n) * n / 2
    endtime = datetime.datetime.now()
    print("function4 runs {} microsecond.".format((starttime - endtime).microseconds))
    return sum


if __name__ == "__main__":
    #print(seq1_1())
    #print(seq1_2())
    print(seq2_1(9999999))
    print(seq2_2(9999999))

