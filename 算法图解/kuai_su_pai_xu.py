"""
快速排序

步骤
1. 递归: 缩小问题规模
2. 基线条件: 数组只有一个或者没有元素不需要排序直接返回元素就可以了
3. 使用第一元素作为基准值
4. 找出所有小于等于记住值的元素
5. 找出所有大于基准值的元素


性能


"""


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        # 第一个元素为基准值
        base_num = arr[0]
        # 所有 <= 基准值得元素
        little = [i for i in arr[1:] if i <= base_num]
        # 所有 > 基准值的元素
        big = [i for i in arr[1:] if i > base_num]
        # 小于基准值 + 基准值 + 大于基准值
        return quick_sort(little) + [base_num] + quick_sort(big)


b_list = [100, 8, 200, 2, 5, 55]
print(quick_sort(b_list))





"""
c 是算法所需的固定时间量，被称为常量.
通常不考虑这个常量，因为如果两种算法的大O运行时间不同，这种常量将无关紧要.

例如
二分查找: 40亿个元素, 常量为10毫秒, 463天
简单查找: 40亿个元素, 常常量为1秒, 32秒



快速排序的性能高度依赖于你选择的基准值。假设你总是将第一个元素用作基准值，且要处
理的数组是有序的。由于快速排序算法不检查输入数组是否有序，因此它依然尝试对其进行排序


"""














