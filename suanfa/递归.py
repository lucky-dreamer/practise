"""
递归，即自己调用自己，，写的时候必须设置基线条件（停止时的条件）和递归条件（递归时的条件)
"""


def count_down(x):
    if x >= 1:       # 基线条件
        print(x)        # 执行的函数体
        count_down(x-1)        # 递归条件


def count_down2(x):     # 同样的例子用循环来写， 结果一样
    while x >= 1:
        print(x)
        x -= 1


# count_down2(99)


def table_9(i, j, list):               # 用递归思路写的99乘法表
    if j<10:    # 终止条件
        if i<10:
            if i <= j:
                s = i * j
                answer = str(i) + '*' + str(j) + '=' + str(s)
                list.append(answer)
                table_9(i+1, j, list)
        print(' '.join(list))
        list.clear()
        table_9(1, j+1, list)
    else:
        exit()


def table_9_2():               # 用循环思路写的99乘法表
    list = []
    for j in range(1, 10):      # 外面的对应后面的数，用来约束每一行
        for i in range(1, 10):  # 里面的对应前面的数，不能超过后面的数
            if i <= j:
                s = i * j
                answer=str(i)+'*'+str(j)+'='+str(s)
                list.append(answer)
        print(' '.join(list))
        list.clear()


table_9(1,1,[])
# table_9_2()





