import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'E'}

mapping = collections.ChainMap(a, b)

for key, value in mapping.items():
    print(f'{key}: {value}')

print(mapping.maps)

# updating values with doubles
mapping['c'] = 'F'

print(mapping.maps)