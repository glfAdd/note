def f(x):
    return x * x


a = [1, 2, 3, 4, 5, 6]
# 收一个函数f和一个list，并通过把函数f依次作用在list的每个元素上，得到一个新的map对象
b = map(f, a)
print(b)
for i in b:
    print(i)
