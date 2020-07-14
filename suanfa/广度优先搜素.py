"""
为了找到解决两样东西最短距离的算法（例子为找到人际圈中关系最近的芒果经销商）
"""
from collections import deque


maps=dict()                                # 利用散列表来创建图从而表示人际圈关系
maps['me']=['BOB','ALICE','CLAIRE']    # 各个节点以及其对应的邻居用键值来表示
maps['BOB']=['ANUJ','PEGGY']
maps['ALICE']=['PEGGY']
maps['CLAIRE']=['THOM','JONNY']
maps['ANUJ']=[]
maps['PEGGY']=[]
maps['JONNY']=[]
maps['THOM']=[]


def search_seller():
    dequen = deque()       # 初始队列
    dequen += maps['me']   # 将第一层关系加入到队列中
    searched = []          # 为了防止查找过的人重复查找，这里把他门放入一个列表中
    while dequen:        # 如果队列不为空
        person = dequen.popleft()  # 最左边的人出队
        if person not in searched:  # 如果这个人没找过
            if person[-1] == 'M':   # 判断是否为seller
                return print(person + ' is a seller')  # 找到了的话就此输出返回
            else:
                dequen += maps[person]  # 不是的话，把这个人的朋友加入到队列当中，队列为先进先出，所以加入到了尾部
                searched.append(person)  # 此人加入查找过的名单中
    return print('nobody')      # 所有队列中都没有此人，则无


search_seller()







