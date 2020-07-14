"""
用Dijkstra 算法计算加权有向图中的最短路径
只要还有节点未被处理，找到最便宜（距离起点最近）的节点，更新它到它邻居的开销，
如果邻居的开销被更新，同时也更新邻居的父节点，将该节点标记为处理过，循环
"""


graph = dict()     # 设置第一个散列表，用于描述该问题的逻辑关系，将图抽象为代码
graph['start'] = dict()  # 在该散列表中，为每个节点设置一个散列表，方便描述它与邻居的关系以及开销
graph['start']['a'] = 6  # start到a的开销
graph['start']['b'] = 2
graph['a'] = dict()
graph['a']['fin'] = 1   # a 到终点的开销
graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['fin'] = 3
graph['fin'] = dict()

cost = dict()                # 由于在使用算法的过程中需要实时更新开销和父节点，用于比较以及路径选择
cost['a'] = 6                                  # 所以需要再设置两个散列表用于记录这两个指标
cost['b'] = 2
cost['fin'] = float('inf')    # 由于不知道终点的开销，所以设为无穷大，，对于目前不能确定的开销，都设置为无穷大

parent=dict()
parent['a'] = 'start'
parent['b'] = 'start'
parent['fin'] = None       # 对于不确定的都设置为空
processed = []            # 记录处理过的节点，避免重复处理
                           # 以上完成了初始的抽象设置，接下来进行逻辑实现


def find_smallest_cost_node(cost):   # 找最低开销的节点
    smallest_cost=float('inf')       # 假设最大的节点的开销为最低开销
    smallest_cost_node=None           # 最低开销的节点为空
    for node in cost:                # 在所有节点的开销中
        cost1=cost[node]              # 拿到各个节点开销
        if cost1 < smallest_cost and node not in processed:  # 如果该开销比最小开销低，且没验证过该节点
            smallest_cost_node=node         # 该节点为最便宜的节点
            smallest_cost=cost1               # 该节点的开销赋值给最小开销
    return smallest_cost_node


def Dijkstra():
    node=find_smallest_cost_node(cost)    # 找到当前最小开销点
    while node:                           # 如果存在
        neibor=graph[node].keys()         # 找他的所有邻居
        cost_node=cost[node]               # 拿到我的开销
        for x in neibor:
            new_cost=graph[node][x]+cost_node  # 邻居的新开销等于我的开销加我到邻居的开销
            if new_cost < cost[x]:           # 如果邻居的新开销比以前的开销便宜
                cost[x]=new_cost            # 那么把邻居的新开销赋值给邻居开销
                parent[x]=node              # 同时把邻居父节点更新为当前节点
        processed.append(node)              # 把当前节点标为已经验证
        node = find_smallest_cost_node(cost)  # 继续找下一个最便宜节点
    print(parent)                             # 输出路径

Dijkstra()