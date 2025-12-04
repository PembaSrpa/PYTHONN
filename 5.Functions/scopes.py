# Scope refers to the region of code where a variable is accessible.

# Example 1: Local vs. global variable
x = 10  # Global variable

def show_scope():
    x = 5  # Local variable
    print("Inside function, x =", x)

show_scope()
print("Outside function, x =", x)

# Example 2: The 'global' keyword
count = 0

def increment():
    global count
    count += 1
    print("Inside function, count =", count)

increment()
print("Outside function, count =", count)

# Example 3: Nested functions and 'nonlocal' keyword
def outer():
    msg = "outer scope"

    def inner():
        nonlocal msg
        msg = "modified by inner"
        print("Inside inner:", msg)

    inner()
    print("Inside outer:", msg)

outer()