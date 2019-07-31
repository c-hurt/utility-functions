mapping_zipped = zip(['a', 'b', 'c', 'd'], [100, 90, 99, 87])

for key, value in mapping_zipped:
    print(f'{key}: {value}')

mapping_zipped_list = list(zip(['e', 'g'], [1200, 900]))

print(mapping_zipped_list)