import time
from threading import Thread


class RefreshScheduler:
    def __init__(self, delay):
        self.delay = delay
        self.waiting = False

    def _delay(self, callback):
        print("A rebuild is currently scheduled.")
        time.sleep(self.delay)
        callback()
        self.waiting = False

    def request_refresh(self, callback):
        if self.waiting:
            return

        self.waiting = True
        t = Thread(target=self._delay, args=(callback,))
        t.start()
