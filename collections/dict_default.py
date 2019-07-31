import collections

def default_value():
    return 0

paging = collections.defaultdict(default_value, more=10)

print(paging)
print(paging['last'])
print(paging)