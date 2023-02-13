"""
gather

https://www.pythonf.cn/read/318

不同的执行结果
1. 不注释 await evaluate_work(task)
evaluation: starting...
do_some_work:  0
work evaluation returned:  some_work is done for 0
evaluation: starting...
do_some_work:  1
work evaluation returned:  some_work is done for 1
evaluation: starting...
do_some_work:  2
work evaluation returned:  some_work is done for 2
evaluation: starting...
do_some_work:  3
work evaluation returned:  some_work is done for 3
evaluation: starting...
do_some_work:  4
work evaluation returned:  some_work is done for 4
Task result: some_work is done for 0
Task result: some_work is done for 1
Task result: some_work is done for 2
Task result: some_work is done for 3
Task result: some_work is done for 4
total run time: 10.010937213897705


2. 注释后 await evaluate_work(task)
do_some_work:  0
do_some_work:  1
do_some_work:  2
do_some_work:  3
do_some_work:  4
Task result: some_work is done for 0
Task result: some_work is done for 1
Task result: some_work is done for 2
Task result: some_work is done for 3
Task result: some_work is done for 4
total run time: 2.002945899963379

"""
import time
import asyncio

now = lambda: time.time()


async def do_some_work(x):
    print("do_some_work: ", x)
    await asyncio.sleep(2)
    return "some_work is done for {}".format(x)


async def evaluate_work(task):
    print('evaluation: starting...')
    result = await task
    print("work evaluation returned: ", result)


async def main():
    tasks = []
    for i in range(5):
        work_coroutine = do_some_work(i)
        task = asyncio.ensure_future(work_coroutine)
        tasks.append(task)
        # 注释后结果不同
        await evaluate_work(task)
    results = await asyncio.gather(*tasks)
    for result in results:
        print("Task result:", result)


start = now()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
loop.close()
end = now()
print("total run time:", end - start)
