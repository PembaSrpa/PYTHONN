
class Person:
    def __init__(self, name, age):
        self.name = name    # Instance attribute
        self.age = age      # Instance attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Usage:
person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.