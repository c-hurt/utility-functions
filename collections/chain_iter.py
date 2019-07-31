from itertools import *

def yielding_iter():
    for a in range(0,10):
        yield [a]

for a in chain.from_iterable(yielding_iter()):
    print(f'{a} ')