import queue
import functools
import threading
import random

queue_fifo = queue.Queue()
queue_lifo = queue.LifoQueue()
queues = {queue_fifo, queue_lifo}

for a in range(0, 20):
    queue_fifo.put(a)
    queue_lifo.put(a)

for a in queues:
    while not a.empty():
        print(f'{a.get() }')
    print('\n')

# priority queue
@functools.total_ordering
class Ordering:
    def __init__(self, priority, desc):
        self.priority = priority
        self.desc = desc
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented

#implementing priority queue
p_queue = queue.PriorityQueue()

qty = 20
min_level = 0
max_level = 20
desc = ['Low', 'Med', 'High', 'Max']
queue_priority = queue.PriorityQueue()
#desc_select = []
#levels = []

for a in range(0, qty):
    desc_select = random.randint(0, len(desc) - 1)
    level = random.randint(min_level, max_level - 1)
    queue_priority.put(Ordering(level, desc[desc_select]))

# consumption of pqueue threading
def process_ordering(queue):
    while True:
        order_next = queue.get()
        print(f'Working order: {order_next.desc}')
        queue.task_done()

threads_workers = [
    threading.Thread(target=process_ordering(queue_priority), args=(queue_priority,)),
    threading.Thread(target=process_ordering(queue_priority), args=(queue_priority,))
]

for thread in threads_workers:
    thread.setDaemon(True)
    thread.start()

queue_priority.join()