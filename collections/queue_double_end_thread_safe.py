import collections
import threading
import time
import random

pages = collections.deque(range(20))

def popping(direction, direction_func):
    while True:
        try:
            next_source = direction_func()
        except IndexError:
            break
        else:
            print(f'{direction}: {next_source}')
            # sleep the thread to allow another thread to complete
            time.sleep(random.randint(0,1))
    return

front = threading.Thread(target=popping, args=('front', pages.popleft))
back = threading.Thread(target=popping, args=('back', pages.pop))

front.start()
back.start()

front.join()
back.join()