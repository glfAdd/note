from queue import Queue
from threading import Thread, Event

"""
https://www.jianshu.com/p/9d4a4c63ce6b




"""


class ActorExit(Exception):
    pass


class Actor(object):
    def __init__(self):
        self._thread = Thread()
        self._queue = Queue()

    def send(self, msg):
        self._queue.put(msg)

    def receive(self):
        msg = self._queue.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def stop(self):
        if self._thread.is_alive():
            self.send(ActorExit)

    def start(self):
        if not self._thread.is_alive():
            self._thread = Thread(target=self._bootstrap)
            self._thread.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass

    def run(self):
        while True:
            msg = self.receive()
            print(msg)


# Sample Actor
class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.receive()
            print("Got:", msg)


if __name__ == '__main__':
    p = PrintActor()
    p.start()
    p.send("Hello")
    p.send("World")
    p.stop()
