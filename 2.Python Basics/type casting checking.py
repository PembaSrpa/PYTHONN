# Type Casting, type checking and validation

# Type Casting is the process of converting a value from one data type to another.

# Type checking is the process of checking the type of a variable.

# Type validation is the process of validating the type of a variable.

# Type casting examples

# Example 1: Converting string to integer before addition
x = 10
y = "20"
z = x + int(y)   # Convert y to int before adding
print(z)         # Output: 30

# Example 2: Converting integer to string for concatenation
a = 5
b = " apples"
result = str(a) + b
print(result)    # Output: 5 apples

# Type checking examples
a = 42
b = "hello"
c = [1, 2, 3]

print(type(a))   # <class 'int'>
print(type(b))   # <class 'str'>
print(type(c))   # <class 'list'>

# Using isinstance() for type validation
x = 3.14
if isinstance(x, float):
    print("x is a float")
else:
    print("x is not a float")

# Example of type validation in a function
def add_integers(i, j):
    if not isinstance(i, int) or not isinstance(j, int):
        print("Both arguments must be integers!")
        return None
    return i + j

print(add_integers(5, 7))        # 12
print(add_integers(5, "seven"))  # Both arguments must be integers! None
