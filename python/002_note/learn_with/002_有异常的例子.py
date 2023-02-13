class Test:
    def __enter__(self):
        print('__enter__() is call!')
        return self

    @staticmethod
    def start():
        print('------------------------------ test')
        return 1 / 0

    def __exit__(self, exc_type, exc_value, traceback):
        """

        @param exc_type:
        @param exc_value:
        @param traceback:
        @return:
            True: 不抛出异常
            False: 抛出异常
        """
        print('__exit__() is call!')
        print(f'exc_type:{exc_type}')
        print(f'exc_value:{exc_value}')
        print(f'traceback:{traceback}')
        print('__exit()__ is call!')
        return True
        # return False


with Test() as t:
    print('------------ 1')
    t.start()
    print('------------ 2')
    raise TypeError
print('------------ 3')
