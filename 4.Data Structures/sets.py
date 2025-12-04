# Sets in Python: Introduction and Operations
# A set is an unordered collection of unique elements.
fruits_set = {'apple', 'banana', 'cherry'}
print(f"Initial set: {fruits_set}")

# Adding items to a set
fruits_set.add('date')
print(f"After adding 'date': {fruits_set}")

# Adding multiple items with update
fruits_set.update(['elderberry', 'fig'])
print(f"After update: {fruits_set}")

# Removing and discarding items
fruits_set.remove('banana')  # Raises KeyError if not present
print(f"After removing 'banana': {fruits_set}")
fruits_set.discard('grape')  # Does nothing if not present
print(f"After discarding 'grape': {fruits_set}")

# Set operations and methods
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union = set_a | set_b
print(f"Union: {union}")

intersection = set_a & set_b
print(f"Intersection: {intersection}")

difference = set_a - set_b
print(f"Difference (A - B): {difference}")

symmetric_difference = set_a ^ set_b
print(f"Symmetric Difference: {symmetric_difference}")

# Set comprehension
squares = {x**2 for x in range(1, 6)}
print(f"Set of squares: {squares}")

# Frozen sets vs set
mutable_set = {10, 20, 30}
frozen = frozenset([10, 20, 30])
print(f"Mutable set: {mutable_set}")
print(f"Frozen set: {frozen}")

# Frozen sets are immutable:
# frozen.add(40)  # Would raise AttributeError