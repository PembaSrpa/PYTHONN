# Base class (Parent)
class Animal:
    def __init__(self, name):
        self._name = name

# Derived class (Child) - Function overriding
class Dog(Animal):
    def speak(self):
        print(f"{self._name} says: Woof!")

animal = Animal("GenericAnimal")
dog = Dog("Buddy")

print(animal._name)      # Output: GenericAnimal
print(dog._name)         # Output: Buddy
dog.speak()              # Output: Buddy says: Woof!
