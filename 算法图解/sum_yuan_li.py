"""
sum原理
1. 接受一个列表, 如果为空返回0
2. 否则计算除第一个数以外其他数的总和, 将其与第一个数相加再返回结果
"""
a_list = [1, 2, 3, 4, 5]


def calculate_sum(arr):
    """自己实现sum功能"""
    if len(arr) == 0:
        return 0
    else:
        if len(arr) == 1:
            return arr[0]
        else:
            a = calculate_sum(arr[1:])
            return arr[0] + a


print(calculate_sum(a_list))
