


"""
gevent在执行时遇到耗时操作自动切换执行别的协程，会交出cpu使用，以此类推. 当所有的协成都到了耗时操作了没的切换了，那就等耗时操作完成. 自动识别哪些操作属于耗时操作. 没有耗时操作不会自动切换. 

#创建一个协程对象g ,spawn括号内第一个参数是函数名，后面可以有多个参数（位置参数，关键字参数）。
g=gevent.spawn(func,1,……,x=3,……)
# 阻塞住,等都执行完了再往后
g.join()
g.value#拿到func的返回值。
# 当前携程
gevent.getcurrent()

# 需要增加这两行来识别time.spleep
from gevent import monkey,spawn
monkey.patch_all()

"""