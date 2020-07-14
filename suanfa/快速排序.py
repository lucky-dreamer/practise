"""
O(nlogn)
"""

def quickly_sort(list_m):   # 快速排序算法

    if len(list_m) < 2:   # 基线条件，如果列表中少于两个数，就不用排序，直接返回列表
        return list_m
    else:                  # 找出基准，小于基准数的数的集合放在左边，大于基准数的集合放在右边
        stan = list_m[0]
        less = [i for i in list_m[1:] if i <= stan]
        more = [i for i in list_m[1:] if i > stan]    # 持续分割两边的区间，直到达到基线条件
    return quickly_sort(less)+[stan]+quickly_sort(more)


print(quickly_sort([1, 5, 69, 20, 54, 21]))