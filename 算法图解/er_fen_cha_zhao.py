"""
简单查找
一个个查找, 最多n次


二分查找
1. 输入有序元素列表, 找到了返回位置, 没找到返回None
2. n个元素的列表二分法最多log2n次
100 -> 50 -> 25 -> 13 -> 7 -> 4 -> 2 -> 1   7次


二分查找的速度比简单查找快得多, 需要搜索的元素越多，前者比后者就快得越多。
"""


def test(all, item):
    start = 0
    end = len(all) - 1
    while start <= end:
        mid = (start + end) // 2
        num = all[mid]
        if num == item:
            return mid
        elif num > item:
            end = mid
        else:
            start = mid
    return None


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(test(a, 5))
