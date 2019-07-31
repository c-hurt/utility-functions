import enum

class Status(enum.Enum):
    new = 10
    exist = 20
    first = 30
    last = 40


for status in Status:
    print(f'{status.name}: {status.value}')