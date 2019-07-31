import shelve

db_name = 'shelve'

with shelve.open(db_name) as f:
    f['naming'] = {
        'name_first': 'josh',
        'name_last': 'hurt'
    }

# reading from the shelved data
data_read = None

with shelve.open(db_name) as f:
    data_read = f['naming']

print(data_read)

# altering shelved data
with shelve.open(db_name, writeback=True) as f:
    f['naming']['name_last'] = 'personify'
    print(f['naming'])