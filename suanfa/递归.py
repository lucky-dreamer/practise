"""
递归，即自己调用自己，，写的时候必须设置基线条件（停止时的条件）和递归条件（递归时的条件)
"""


def count_down(x):
    print(x)  # 执行的函数体
    if x <= 1:       # 基线条件
        return
    else:
        count_down(x-1)        # 递归条件


def count_down2(x):     # 同样的例子用循环来写， 结果一样
    while x >= 1:
        print(x)
        x -= 1


# count_down(99)
# count_down2(99)

# 思路：按行打印
def table_9(i, j, list):                 # 用递归思路写的99乘法表
    s = i * j                                 # 行里面的操作，添加，但是暂时不打印出来
    answer = str(i) + '*' + str(j) + '=' + str(s)
    list.append(answer)
    if i == j:               # 第一个基线条件
        print(' '.join(list))     # 满足，则打印行，清空列表，进行下一行的递归打印
        list.clear()
    else:                     # 如果不满足，则递归继续往列表里加东西,前面的数字逐渐增大到和后面一样
        table_9(i + 1, j, list)
    if j == 9:               # 打印完一行了之后，如果满足了9行的要求，就退出
        exit()
    else:                    # 没有的话，行再增加，递归
        table_9(1, j + 1, list)


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


# table_9(1,1,[])
# table_9_2()


def sum1(x):
    if x == []:        # 最后一个为加零
        return 0
    return x[0]+sum1(x[1:])   # 返回列表第一个数加列表后面的，不断拆后面的列表知道拆到最后为零，即所有元素相加


# print(sum1([1,3,5,45]))


def count_item(list_p):
    if list_p == []:
        return 0
    return 1+count_item(list_p[1:])

# print(count_item([1,2,3,8,10]))


def max_x(list_d):
    if len(list_d) == 2:
        if list_d[0] > list_d[1]:
            return list_d[0]
        else:
            return list_d[1]
    sub_list = max_x(list_d[1:])
    if list_d[0] > sub_list:
        return list_d[0]
    else:
        return sub_list


# print(max_x([1,2,8,98]))


