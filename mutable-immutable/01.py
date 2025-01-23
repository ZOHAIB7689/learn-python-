# Demonstrating mutable and immutable types in Python

# Immutable type: int
a = 10
print(f"Initial value of a: {a}")
a = 20
print(f"Modified value of a: {a}")

# Immutable type: string
s = "hello"
print(f"Initial value of s: {s}")
s = "world"
print(f"Modified value of s: {s}")

# Mutable type: list
lst = [1, 2, 3]
print(f"Initial list: {lst}")
lst.append(4)
print(f"Modified list: {lst}")

# Mutable type: dictionary
d = {'key1': 'value1'}
print(f"Initial dictionary: {d}")
d['key2'] = 'value2'
print(f"Modified dictionary: {d}")