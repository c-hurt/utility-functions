import pickle
import pprint

data_a = [{'e': 10, 'g': 1200}]
data_pickle = pickle.dumps(data_a)
data_pickle_load = pickle.loads(data_pickle)[0]

print(data_a)
print(data_pickle_load['g'])

# pickle streams
import io

class Pickled:
    def __init__(self, name):
        self.name = name
        self.name_rev = name[::-1]
        return

data_pickle = []
data_pickle.append(Pickled('place'))
data_pickle.append(Pickled('normal'))
output = io.BytesIO()

for a in data_pickle:
    print(f'Writing: {a.name}, rev: {a.name_rev}')
    pickle.dump(a, output)
    output.flush()

input = io.BytesIO(output.getvalue())

while True:
    try:
        value = pickle.load(input)
    except EOFError:
        break
    else:
        print(f'Value read: {value.name}, rev: {value.name_rev}')
