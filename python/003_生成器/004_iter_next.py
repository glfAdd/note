class Test1:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 10:
            raise StopIteration
        else:
            self.num += 1
            return self.num


class Test2:
    def __init__(self, num):
        self.num = num

    # def __iter__(self):
    #     return self

    def __next__(self):
        if self.num > 10:
            raise StopIteration
        else:
            self.num += 1
            return self.num


if __name__ == "__main__":
    t = Test1(7)
    for i in Test1(1):
        print(i)
    for i in Test2(1):
        print(i)
    # for i in range(7):
    #     print(t.__next__())
