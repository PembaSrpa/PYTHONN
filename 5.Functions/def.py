# Example 1: No arguments, simple print
def greet():
    print("Hello, world!")

greet()

# Example 2: Function with arguments and return value
def add(a, b):
    return a + b

result = add(3, 5)
print("Sum:", result)

# Example 3: Function with default arguments
def introduce(name, age=30):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice")
introduce("Bob", 25)

# Example 4: Function with variable-length arguments
def print_numbers(*numbers):
    for number in numbers:
        print("Number:", number)

print_numbers(1, 2, 3, 4)

# Example 5: Function that returns multiple values
def min_and_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_and_max([5, 2, 9, 1])
print("Minimum:", minimum)
print("Maximum:", maximum)