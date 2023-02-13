class Test:
    def __enter__(self):
        print('__enter__() is call!')
        return self

    @staticmethod
    def start():
        print('------------------------------ test')

    def __exit__(self, exc_type, exc_value, traceback):
        """
        如果上下文运行时没有异常发生，那么三个参数都将置为None

        @param exc_type:
        @param exc_value:
        @param traceback:
        @return:
        """
        print('__exit__() is call!')
        print(f'exc_type:{exc_type}')
        print(f'exc_value:{exc_value}')
        print(f'traceback:{traceback}')
        print('__exit()__ is call!')


with Test() as t:
    t.start()
