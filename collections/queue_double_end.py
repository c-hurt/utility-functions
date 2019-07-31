import collections

dq = collections.deque('hereistheentirepiecing')

print(dq)

while True:
    try:
        print(dq.pop())
    except IndexError:
        break

print(dq)

# populating queue
# adding to the queue

next_portion = 'thenextpiece'

dq.extend(next_portion)

while True:
    try:
        print(dq.pop())
    except IndexError:
        break

# adding to the left side of the queue
dq.extendleft('nextPaging')
dq.extend('OfCourseAgain')

print('\n\n-- Last Run --')

while True:
    try:
        print(dq.pop())
    except IndexError:
        break