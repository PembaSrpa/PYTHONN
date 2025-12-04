# overview and fundamental operations
# A list is an ordered, mutable collection of items in Python.
# Lists can store elements of different data types.

# Creating a list
fruits = ['apple', 'banana', 'cherry', 'date']
print(f"Fruits list: {fruits}")

# Indexing, slicing, and negative indexing
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"First two fruits: {fruits[:2]}")
print(f"All except first: {fruits[1:]}")

# Looping through lists and using conditions
for fruit in fruits:
    if 'a' in fruit:
        print(f"Fruit with 'a': {fruit}")
    else:
        print(f"Other fruit: {fruit}")

# List methods and functions
fruits.append('elderberry')
print(f"After append: {fruits}")
fruits.remove('banana')
print(f"After remove: {fruits}")
fruits.sort()
print(f"After sort: {fruits}")
length = len(fruits)
print(f"Number of fruits: {length}")

# List comprehension with conditions
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(f"Fruits with names longer than 5 letters: {long_fruits}")