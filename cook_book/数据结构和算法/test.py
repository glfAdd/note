"""
在字典中将键映射到多个值上
让字典保持有序
在两个字典中寻找相同点
从序列中移除重复项切保持元素间顺序不变
对切片命名
找出序列中出现次数最多的元素
通过公共键对字典列表排序
"""

""" 将序列分解为单独的变量 ----------------------------"""
str_01 = '1234'
a, _, b, _ = str_01
# 对其某些不用的值, 使用一个不用的变量
print(a, b)

""" 保存最后N个元素 ----------------------------"""
# deque 最多N个元素, 满了以后自动移除老的. 不设置为无限制
# 有和list类似的操作 append pop 等
# 输出匹配的当前行和最后查找的N行
from collections import deque


def search(lines, pattern, num=5):
    history = deque(maxlen=num)
    for i in lines:
        if i == pattern:
            yield i, history
        history.append(i)


with open('test.py') as f:
    for i in search(f, 'print(a, b)\n', 5):
        print(i)

""" 最大 / 最小 的N个元素 ----------------------------"""
# todo glfadd 堆的顺序存储
# 从M个元素中找N个元素. 如果M和N相差很大可以使用, 当N为1是可以使用max和min, 让M和N相差很小时可以先排序后切片
import heapq

list_02 = [23, 734, -12, 1, 34, 0, 1, 7, 78, 9]
print(heapq.nlargest(3, list_02))  # [734, 78, 34]
print(heapq.nsmallest(3, list_02))  # [-12, 0, 1]

list_03 = [
    {'name': 'xiao2', 'price': 12},
    {'name': 'xiao3', 'price': 82},
    {'name': 'xiao4', 'price': 4},
    {'name': 'xiao5', 'price': 43},
    {'name': 'xiao6', 'price': 5},
]
print(heapq.nlargest(3, list_03, key=lambda x: x[
    'price']))  # [{'name': 'xiao3', 'price': 82}, {'name': 'xiao5', 'price': 43}, {'name': 'xiao2', 'price': 12}]

""" 优先级队列 ----------------------------"""
