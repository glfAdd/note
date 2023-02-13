""" ============================ 参考
https://zhuanlan.zhihu.com/p/27258289
"""

# 异步函数
# 直接调用异步函数不会返回结果，而是返回一个coroutine协程对象
# <coroutine object async_function at 0x10b9b13c0>
async def async_function():
    return 1


# 异步生成器
async def async_generator():
    yield 1


# await语法来挂起自身的协程，并等待另一个协程完成直到返回结果
# await语法只能出现在通过async修饰的函数中，否则会报SyntaxError错误
# await后面的对象需要是一个Awaitable，或者实现了相关的协议
async def await_coroutine():
    result = await async_function()
    print(result)


def run(coroutine):
    # 生成器/协程在正常返回退出时会抛出一个StopIteration异常
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value


run(await_coroutine())
