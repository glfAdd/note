"""
1. 未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 以此类推，直到所有元素均排序完毕

时间复杂度: O(n2)
n x n x 1/2 去掉常量1/2
"""

"""================方式1: pop最小的放进新的list"""


def search_min_index(alist):
    """获取最小值index"""
    # 假设第一个是最小的
    min_index = 0
    num = alist[0]
    for index, value in enumerate(alist):
        if value < num:
            num = value
            min_index = index
    return min_index


def sort_list(arr):
    new_list = []
    for i in range(len(arr)):
        index = search_min_index(arr)
        new_list.append(arr.pop(index))
    return new_list


prime_list = [123, 4545, 6, 123333, 5, 7]
print(sort_list(prime_list))
"""================方式2: 找到最小的和最前面的交换位置"""


def sort_list2(arr):
    for i in range(len(arr)):
        # 假设第一个是最小的
        min_index = i
        min_num = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min_num:
                min_index = j
                min_num = arr[j]
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


prime_listr2 = [123, 4545, 6, 123333, 5, 7]
sort_list2(prime_listr2)
print(prime_listr2)
