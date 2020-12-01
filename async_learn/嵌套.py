"""

https://stackoverflow.com/questions/36342899/asyncio-ensure-future-vs-baseeventloop-create-task-vs-simple-coroutine

改变 await task的位置执行的结果不一样

first
long_operation started
second
long_operation finished


first
long_operation started
long_operation finished
second
"""
import asyncio


async def msg(text):
    await asyncio.sleep(0.1)
    print(text)


async def long_operation():
    print('long_operation started')
    await asyncio.sleep(3)
    print('long_operation finished')


async def main():
    await msg('first')

    # Now you want to start long_operation, but you don't want to wait it finised:
    # long_operation should be started, but second msg should be printed immediately.
    # Create task to do so:
    task = asyncio.ensure_future(long_operation())

    # Now, when you want, you can await task finised:
    await task

    await msg('second')

    # Now, when you want, you can await task finised:
    # await task


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
