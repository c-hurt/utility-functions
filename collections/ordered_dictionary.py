import collections

dict_a = collections.OrderedDict()

dict_a['e'] = 10
dict_a['r'] = 1200
dict_a['b'] = 12
dict_a['g'] = 19

for key, value in dict_a.items():
    print(f'{key}: {value}')

# reordering ordered dictionary
dict_a.move_to_end('e', True)
dict_a.move_to_end('g', False)

print('\n\n\n\n')

for key, value in dict_a.items():
    print(f'{key}: {value}')