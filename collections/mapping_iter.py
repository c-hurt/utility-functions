from itertools import *

def mult_double(a):
    return 2 * a

def tuple_mult(a, b):
    return (a, b, a * b)


for a in map(tuple_mult, range(10), range(5)):
    print(a)

# filtering
def dropping(a):
    return a < 100

for a in dropwhile(dropping, [1, 90, 80, 1, 12, 1200]):
    print(a)