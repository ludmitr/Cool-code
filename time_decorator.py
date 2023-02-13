import time
import signal
import threading
import functools

class Alarm:
    """
        Do a time count down and will raise a TimeoutError
        
        Parameters:
        interval(int or float): the number to countdown - > raise temouterror
    """
    def __init__(self, interval):
        self.interval = interval
        self.timer = None

    def start(self):
        self.timer = threading.Timer(self.interval, self.raise_error)
        self.timer.start()

    def stop(self):
        self.timer.cancel()

    def raise_error(self):
        raise TimeoutError("it ran more than {} seconds".format(self.interval))

def timeout(func):
    """
    Will raise timeouterror if a function run longer than 5 sec
    """
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        a = Alarm(5)
        a.start()
        try:
            func()
        except TimeoutError as e:
            raise e
        finally:
            a.stop()
            
    return wrapper

@timeout
def func_one():
    time.sleep(1)
    print("func one finished")
@timeout
def func_two():
    time.sleep(6)
    print("func two finished")



func_two()
