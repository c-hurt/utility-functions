import collections

# using the counter method
counting = collections.Counter('aeffeerttuvaabfe        ')
counting_more = collections.Counter('here is the longest      subset')

counting.update({'b': 23, 'z': 10})
letters = 'efrtyu'

print(counting)

# iterating over the counts
for value in letters:
    print(f'{value}: {counting[value]}')

# get most common counts
for value, common in counting.most_common(10):
    print(f'{value}: {common}')

for value in counting_more:
    print(f'{value}: {counting_more[value]}')

# merging different counts
counting_all = counting + counting_more

for value in counting_all:
    print(f'{value}: {counting_all[value]}')