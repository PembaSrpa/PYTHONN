# Functions can take parameters (inputs), which are specified in the function definition.
# You can pass arguments to these parameters when calling the function.
# Functions can also return a value using the 'return' statement.

# Example 1: Function with parameters
def multiply(a, b):
    # 'a' and 'b' are parameters
    result = a * b
    return result  # Returns the product

product = multiply(4, 5)  # 4 and 5 are arguments
print("Product:", product)

# Example 2: Parameters with default values
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Uses default greeting
print(greet("Bob", "Hi"))       # Overrides default

# Example 3: Variable-length positional arguments using *args
def sum_all(*args):
    # args is a tuple of all positional arguments passed
    return sum(args)

print("Sum of 1, 2, 3:", sum_all(1, 2, 3))
print("Sum of 10, 20:", sum_all(10, 20))

# Example 4: Variable-length keyword arguments using **kwargs
def describe_person(name, **kwargs):
    # kwargs is a dictionary of keyword arguments
    description = f"Name: {name}"
    for key, value in kwargs.items():
        description += f", {key}: {value}"
    return description

print(describe_person("Alice", age=30, city="New York"))

# Example 5: Returning multiple values
def get_min_max(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    return min_val, max_val

numbers = [3, 7, 1, 9, 2]
minimum, maximum = get_min_max(numbers)
print(f"Min: {minimum}, Max: {maximum}")
