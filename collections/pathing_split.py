import os.path

PATH = [
    'a/b/c/last.open',
    'e/f/g/more'
]

for path in PATH:
    print(f'{path}, split: {os.path.split(path)}')

# get basename of path
for path in PATH:
    print(f'{path}, basename: {os.path.basename(path)}')

# get dirname of path
for path in PATH:
    print(f'{path}, dirname: {os.path.dirname(path)}')

# splitting text filetype
for path in PATH:
    print(f'{path}, splittext: {os.path.splitext(path)}')