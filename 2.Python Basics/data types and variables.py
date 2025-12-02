# Data Type and Variables

# What are Data Types?
# Data types specify the type of value that a variable holds.
# Some common data types in Python:

# Integer (int)
age = 25

# Floating point (float)
pi = 3.14159

# String (str)
name = "Alice"

# Boolean (bool)
is_student = True

# NoneType
nothing = None

# List: an ordered collection of items
fruits = ["apple", "banana", "cherry"]

# Tuple: an ordered, immutable collection
coordinates = (10, 20)

# Dictionary: a collection of key-value pairs
person = {
    "name": "Bob",
    "age": 30
}

# Set: an unordered collection of unique items
unique_numbers = {1, 2, 3}

# What are Variables?
# Variables are used to store data in memory. The value stored in a variable can be changed during program execution.

# Assigning variables
x = 5
y = "hello"
z = 8.6

# You don't need to declare a variable's type. Python figures it out automatically.

# You can check the type of any variable using the type() function:
print(type(age))        # <class 'int'>
print(type(pi))         # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>
print(type(nothing))    # <class 'NoneType'>
print(type(fruits))     # <class 'list'>
print(type(coordinates))# <class 'tuple'>
print(type(person))     # <class 'dict'>
print(type(unique_numbers)) # <class 'set'>



