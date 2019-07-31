import collections

User = collections.namedtuple('User', 'password cart')

user_a = User(password='39393', cart=20)

print(user_a)

# converting name tuple -> ordered dictionary
user_a_named_dict = user_a._asdict()

print(user_a_named_dict)

print(user_a_named_dict['cart'])

# updating named tuple value with new object reference
user_a_alter = user_a._replace(cart=1200)

print(user_a_alter)