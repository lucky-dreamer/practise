"""
实现二分法必须在有序列表的前提下进行，快速排序法是一种进行排序的方法
"""


def find_smallest(list1):  # 找到最小的元素，
    smallest = list1[0]
    for i in list1:
        if i < smallest:
            smallest = i
    return smallest


def quick_sort(list1):  # 把最小的元素加入到新的列表，再在原列表中删除这个元素，最后返回新的列表
    new_list = []
    for k in range(len(list1)):     # 这里要把原来列表中所有元素加到新的列表中，所以必须是原列表的长度，由于列表中的元素会变化，所以不能便利列表的元素
        small = find_smallest(list1)
        new_list.append(small)
        list1.remove(small)
    return new_list


print(quick_sort([1, 8, 4, 6, 87, 125, 44, 32]))
