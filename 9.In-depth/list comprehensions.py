# List comprehensions are a concise way to create lists in Python.
# They provide a more syntactically compact and often faster alternative to for-loops for generating new lists.

# Basic syntax:
# [expression for item in iterable if condition]

# Example 1: Generate the squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print("Squares from 0 to 9:", squares)

# Example 2: Select only even numbers from 0 to 19
evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers from 0 to 19:", evens)

# Example 3: Create a list of lowercase strings from a list, filtering out short words
words = ["Hello", "to", "the", "WORLD", "of", "PYTHON"]
long_words_lower = [w.lower() for w in words if len(w) > 3]
print("Lowercased words longer than 3 characters:", long_words_lower)

# Example 4: Flattening a 2D list (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [item for row in matrix for item in row]
print("Flattened matrix:", flattened)

# Example 5: Creating a dictionary from two lists using a comprehension
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_comp = {k: v for k, v in zip(keys, values)}
print("Dictionary from two lists:", dict_comp)

# List comprehensions can also be nested, though readability can suffer:
# Example 6: Multiplying each number in a matrix by 2
doubled_matrix = [[item * 2 for item in row] for row in matrix]
print("Matrix with elements doubled:", doubled_matrix)

# In summary:
# - List comprehensions are powerful and expressive, ideal for transforming and filtering data in lists.
# - You can also create sets ({...}) and dictionaries ({k: v for ...}) using similar comprehensions.
