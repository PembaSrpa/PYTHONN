# introduction to tuples and their operations
# A tuple is an ordered, immutable collection of items in Python.
# Tuples can store elements of different data types.
# They are defined using parentheses: ( )

# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana")
print("Tuple:", my_tuple)

# Indexing, slicing, and iterating through tuples
print("First element:", my_tuple[0])
print("Elements from 2nd to 4th:", my_tuple[1:4])
for item in my_tuple:
    print("Tuple item:", item)

# List vs Tuple: Lists are mutable, tuples are immutable
my_list = [1, 2, 3]
try:
    my_tuple[0] = 10   # This will raise an error
except TypeError:
    print("Tuples are immutable, cannot modify elements.")

my_list[0] = 10
print("Modified list:", my_list)

# Convert between list and tuple
list_to_tuple = tuple(my_list)
print("List to tuple:", list_to_tuple)

tuple_to_list = list(my_tuple)
print("Tuple to list:", tuple_to_list)

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)