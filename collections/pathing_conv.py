import os
import os.path

PATH = [
    '/here/there/okay',
    '/her/there/oka',
    '/here/there/again'
]

prefix_common = os.path.commonprefix(PATH)

print(prefix_common)

# path building
print(os.path.expanduser('~c3p0'))

# getting env var
os.environ['NEW']='lasting'
print(os.path.expandvars('$NEW'))