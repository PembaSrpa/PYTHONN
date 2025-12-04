# --- Polymorphism Example ---

class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()   # Each object calls its own version of 'speak'

# --- Operator Overloading Example ---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Nicely print the point
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Uses __add__
print(p3)     # Output: Point(6, 8)

# Operator overloading is a feature in Python (and some other programming languages)
# that allows developers to define the behavior of built-in operators (like +, -, *, ==, etc.)
# for user-defined classes. By implementing special methods such as __add__, __sub__, __eq__, etc.,
# a class can specify how its objects should respond to these operators.
#
# This makes custom objects behave more like built-in types, making code more intuitive and expressive.
# For example, the Point class above overloads the '+' operator using the __add__ method,
# so that two Point objects can be added together with the '+' symbol.



