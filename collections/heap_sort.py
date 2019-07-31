import heapq
import random

def heap_add(values, heap):
    for a in range(0, len(values)):
        heapq.heappush(heap, values[a])

def heap_print(heap):
    while heap:
        print(heapq.heappop(heap))

data = []
data_secondary = list(random.sample(range(0, 100), 30))
length = 20
min_value, max_value = (0, 100)
heap_init = []

for a in range(0, 20):
    data.append(random.randrange(min_value, max_value))

heap_add(data, heap_init)

print(data)
print(heap_init)

heap_print(heap_init)

# merging heaps
data_total = heapq.merge(data, data_secondary)

print('\n\n\n\n')

for a in data_total:
    print(a)