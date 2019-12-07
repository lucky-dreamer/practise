"""
作者：lucky
功能：输入一段字符串，输出字符串中连续最多的子字符串,如果没有重复的，输出最左边的字符串
"""


def main():
    a = input()  # 输入
    sd = list(a)  # 变成列表形式
    s = {}        # 字典，用于等下存放排列字符串次数排好的键值对
    g = []        # 空列表，用于连接统计好次数的数据
    for i in range(len(a)-1):  # 遍历到倒数第二个字符就好，所以是len（a）-1
        j = i+1
        while sd[i] == sd[j]:  # 当前面值等于后一个值时，比较值继续向后推移
            j = j+1
            if j == len(a):    # 防止最后一次比较报错，此时比较到最后需要终止
                break
        for l in sd[i:j]:
            s[l] = s.get(l, 0) + 1  # 从 i 到 j 前一个数都是相等的，所以统计他们的次数并且构造字典
        km = list(s.items())        # 上述字典列表化，方便等下排序
        s.clear()                   # 字典只是中介，每次存完需要清空，不然会影响次数的统计
        g = g+km                    # 数据存入列表
    g.sort(key=lambda x: x[1], reverse=True)   # 按次数从高到底排序
    x = g[0][1]                                 # 连续最多字符串的次数
    if x == 1:
        print(sd[0])                           # 如果没有重复的，输出最左边的字符串
    else:
        f = ''                                     # 空字符串初值
        for gb in range(x):                        # 字符串有多长，就依次连接起来
            q = g[0][0]
            f = f+q
        print(f)                                   # 打印输出，，，，over!


if __name__ == "__main__":
    main()
