aa = [['74', '9'], ['75', '9'], ['76', '9'], ['77', '9']]
for i in aa:
    print(i)
    b = ','.join(i)
    print(b)

c = '),('.join(','.join(i) for i in aa)
print(c)
