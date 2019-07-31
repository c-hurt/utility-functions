import os.path
import time

print(__file__)
print(f'access time: {time.ctime(os.path.getatime(__file__))}')
print(f'modified time: {time.ctime(os.path.getmtime(__file__))}')
print(f'change time: {time.ctime(os.path.getctime(__file__))}')
print(f'{__file__} size: {os.path.getsize(__file__)}')