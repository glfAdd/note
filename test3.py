def test(a=[]):
    print(a)
    a.append(3)

def test2(a=None):
    if not a:
        a = []
    print(a)
    a.append(4)
test2()
test2()
test2()

