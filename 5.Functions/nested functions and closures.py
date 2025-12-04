# Nested functions are functions defined within other functions.
# Closures occur when a nested function remembers the values from its enclosing scope.

def outer_function(text):
    message = text

    def inner_function():
        # inner_function is a closure because it uses 'message' from the outer scope
        print("Message from inner:", message)

    return inner_function

my_closure = outer_function("Hello from the closure!")
# my_closure remembers the value of 'message', even though outer_function has finished
my_closure()

# Example: Using closures to create custom multiplier functions
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double 5:", double(5))    # Output: 10
print("Triple 5:", triple(5))    # Output: 15

