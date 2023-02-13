from concurrent.futures import ThreadPoolExecutor
import time

"""
线程池





"""


def sayhello(a):
    print(a)
    time.sleep(2)


def main():
    a = ThreadPoolExecutor(2)
    a.submit(sayhello, 1)
    a.submit(sayhello, 2)
    a.submit(sayhello, 3)
    a.submit(sayhello, 4)
    a.submit(sayhello, 5)
    a.submit(sayhello, 6)


if __name__ == '__main__':
    main()
