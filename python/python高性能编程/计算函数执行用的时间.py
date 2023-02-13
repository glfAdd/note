import time
from functools import wraps


def func_cast_time(func):
    @wraps(func)
    def cast_time(*args, **kwargs):
        t_begin = time.time()
        result = func(*args, **kwargs)
        t_end = time.time()
        print(t_end - t_begin)
        return result

    return cast_time


@func_cast_time
def test():
    time.sleep(2)


test()
