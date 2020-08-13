""" ============================
协程(coroutine)不等于异步(asynchonous)，这种方法并不能将原来不支持异步的操作变成异步操作

比如time.sleep()这个非异步的操作，即使将它包装为协程，它还是异步阻塞的
如果想要通过协程实现异步提升I/O效率，正确的做法是使用实现了异步协议的库，而不是思考如何将『普通操作』包装成协程
"""

import asyncio
import time


async def non_asyn_sleep(i):
    time.sleep(1)
    print("Synchonous coroutine {} sleeps 1s".format(i))


async def asyn_sleep(i):
    await asyncio.sleep(1)
    print("asynchonous coroutine {} sleep 1s".format(i))


def supervisor(f):
    t0 = time.time()
    futures = [f(i) for i in range(5)]
    wait_list = asyncio.wait(futures)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_list)
    print("Time Elapsed: {:.3}s\n".format(time.time() - t0))


if __name__ == "__main__":
    supervisor(non_asyn_sleep)
    supervisor(asyn_sleep)
