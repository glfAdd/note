"""




"""


class Person(object):
    def test(self):
        print("---Person---")


class Student(Person):
    def test(self):
        print("---Sutdent---")


def star(temp):
    temp.test()


a = Person()
b = Student()
star(a)
star(b)
