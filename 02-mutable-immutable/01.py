# Demonstrating mutable and immutable types in Python

# Immutable type: int
a = 10
print(f"Initial value of a: {a}")
# Reassigning a new value to 'a' creates a new integer object
a = 20
print(f"Modified value of a: {a}")
# Explanation: Integers are immutable, so when we assign a new value to 'a', 
# a new integer object is created and 'a' now references this new object.

# Immutable type: string
s = "hello"
print(f"Initial value of s: {s}")
# Reassigning a new value to 's' creates a new string object
s = "world"
print(f"Modified value of s: {s}")
# Explanation: Strings are immutable, so when we assign a new value to 's', 
# a new string object is created and 's' now references this new object.

# Mutable type: list
lst = [1, 2, 3]
print(f"Initial list: {lst}")
# Modifying the list in place, the list object itself is changed
lst.append(4)
print(f"Modified list: {lst}")
# Explanation: Lists are mutable, so when we modify the list (e.g., using append), 
# the same list object is changed in place.

# Mutable type: dictionary
d = {'key1': 'value1'}
print(f"Initial dictionary: {d}")
# Modifying the dictionary in place, the dictionary object itself is changed
d['key2'] = 'value2'
print(f"Modified dictionary: {d}")
# Explanation: Dictionaries are mutable, so when we modify the dictionary (e.g., adding a new key-value pair), 
# the same dictionary object is changed in place.