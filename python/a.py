a = []
for i in range(3):
    def func(x):
        return x * i


    a.append(func())

for j in a:
    print(j)
