import asyncio


def test():
    async def run_1():
        await asyncio.sleep(3)
        print('run 1')
        return 'run 1'

    async def run_2():
        await asyncio.sleep(1)
        print('run 2')
        return 'run 2'

    async def run_3():
        await asyncio.sleep(1)
        print('run 3')
        return 'run 3'

    loop = asyncio.get_event_loop()
    # 第一种
    task = [
        run_1(),
        run_2(),
        run_3()
    ]
    # 等待最晚的一个结束才继续执行
    loop.run_until_complete(asyncio.wait(task))
    print('all over 1')

    # 第二种. 遍历task_2获取返回值
    task_2 = [
        loop.create_task(run_1()),
        loop.create_task(run_2()),
        loop.create_task(run_3()),
    ]
    loop.run_until_complete(asyncio.wait(task_2))
    for i in task_2:
        print(i.result())
    print('all over 2')

    loop.close()


if __name__ == '__main__':
    test()
