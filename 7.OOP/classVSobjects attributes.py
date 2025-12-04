# Demonstrating Class (Static) Attributes vs Object (Instance) Attributes

class Dog:
    # Class attribute: shared by all instances
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes: unique to each instance
        self.name = name
        self.age = age

# Creating instances (objects) of Dog
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Accessing class attribute via class and instances
print(Dog.species)    # Output: Canis familiaris
print(dog1.species)   # Output: Canis familiaris
print(dog2.species)   # Output: Canis familiaris

# Accessing instance attributes
print(dog1.name, dog1.age)  # Output: Buddy 3
print(dog2.name, dog2.age)  # Output: Lucy 5

# Changing class attribute via class
Dog.species = "Canis lupus familiaris"
print(dog1.species)   # Output: Canis lupus familiaris

# Changing class attribute via an instance creates an instance attribute (does not affect the class!)
dog1.species = "Unknown"
print(dog1.species)   # Output: Unknown
print(dog2.species)   # Output: Canis lupus familiaris

# Inspect attributes
print(dog1.__dict__)  # Instance attributes + per-instance override: {'name': 'Buddy', 'age': 3, 'species': 'Unknown'}
print(dog2.__dict__)  # Instance attributes only: {'name': 'Lucy', 'age': 5}

# 1. Class attributes are shared across all instances of the class.
# 2. Instance attributes are unique to each object (instance) created from the class.
# 3. Changing a class attribute via the class name affects all instances that have not overridden that attribute.
# 4. Changing a class attribute via an instance creates a new instance attribute, leaving the class-level attribute unchanged for other instances.
# 5. Use `__dict__` to inspect what attributes actually belong to an object instance.
# 6. Class attributes are useful for constants or properties common to all objects, while instance attributes should be used for data unique to each object.
