# Function Overriding and Encapsulation Example

# Base class (Parent)
class Animal:
    def __init__(self, name):
        self._name = name       # Protected attribute by convention (single underscore)

    def speak(self):
        print("The animal makes a sound.")

    def get_name(self):
        return self._name    # Public method to access the "private" attribute

# Derived class (Child) - Function overriding
class Dog(Animal):
    def speak(self):
        print(f"{self._name} says: Woof!")   # This overrides Animal.speak()

# Encapsulation example with private attribute
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color   # Name mangling for "private" attribute

    def speak(self):
        print(f"{self._name} says: Meow!")

    # Public getter for the encapsulated attribute
    def get_color(self):
        return self.__color

    # Public setter for the encapsulated attribute
    def set_color(self, new_color):
        self.__color = new_color

# Demonstration
animal = Animal("GenericAnimal")
dog = Dog("Rex")
cat = Cat("Whiskers", "black")

animal.speak()    # Output: The animal makes a sound.
dog.speak()       # Output: Rex says: Woof!    (Function Overriding)
cat.speak()       # Output: Whiskers says: Meow! (Function Overriding)

# Encapsulation demonstration
print(cat.get_color())    # Output: black
cat.set_color("white")
print(cat.get_color())    # Output: white

# Accessing protected vs. private attributes
print(dog._name)           # Possible (by convention, protected)
# print(cat.__color)       # This will raise AttributeError
print(cat._Cat__color)     # Name mangling can still access "private" attribute, but it's discouraged

