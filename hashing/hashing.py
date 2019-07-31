import hashlib

# hashing available
print(hashlib.algorithms_guaranteed)
print(hashlib.algorithms_available)

# hashing data

lorem = '''Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.'''

hashing = hashlib.md5()
hashing.update(lorem.encode('utf-8'))
print(hashing.hexdigest())

# hashing with sha1
hashing_sha = hashlib.sha1()
hashing_sha.update(lorem.encode('utf-8'))
print(hashing_sha.hexdigest())

# incrementally digest data
def digest_chunk(chunk_size, text):
    starting = 0
    while starting < len(text):
        chunking = text[starting:starting + chunk_size]
        yield chunking
        starting += chunk_size
    return

hashing = hashlib.md5()

for chunk in digest_chunk(128, lorem):
    hashing.update(lorem.encode('utf=8'))

print(hashing.hexdigest())