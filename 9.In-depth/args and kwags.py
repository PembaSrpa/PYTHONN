# Example: Using *args and **kwargs in function definitions

def example_function(required_arg, *args, **kwargs):
    """
    Demonstrates the use of positional arguments, *args, and **kwargs.

    - required_arg: a required positional argument
    - *args: additional positional arguments as a tuple
    - **kwargs: additional keyword arguments as a dict
    """
    print(f"Required argument: {required_arg}")
    print(f"Additional positional arguments (*args): {args}")
    print(f"Additional keyword arguments (**kwargs): {kwargs}")

# Example usages:
example_function(1)
example_function(1, 2, 3, 4)
example_function(1, 2, 3, x=10, y=20)

# You can also unpack iterables and dictionaries:
args = (100, 200)
kwargs = {"foo": "bar", "baz": 42}
example_function("hello", *args, **kwargs)

# 
# The *args syntax allows a function to accept any number of additional positional arguments, which are packed into a tuple. 
# The **kwargs syntax allows a function to accept any number of additional keyword arguments, which are packed into a dictionary.
# This is useful when we don't know beforehand how many arguments will be passed to the function, or when we want to write flexible APIs.