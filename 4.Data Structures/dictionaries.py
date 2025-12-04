# Dictionaries in Python: Introduction and Operations

# A dictionary is a collection of key-value pairs in Python.

# Creating a dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"Person dictionary: {person}")

# Accessing values
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Adding or updating values
person['email'] = 'alice@example.com'
person['age'] = 31
print(f"Updated dictionary: {person}")

# Removing a key-value pair
removed_age = person.pop('age')
print(f"Removed age ({removed_age}): {person}")

# Dictionary methods
keys = list(person.keys())
values = list(person.values())
items = list(person.items())
print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Items: {items}")

# Dictionary comprehension
squares = {}
for x in range(1, 6):
    squares[x] = x ** 2
print(squares)

# Nested dictionaries
students = {
    'student1': {'name': 'John', 'grades': [88, 92]},
    'student2': {'name': 'Emily', 'grades': [91, 85]},
}
print("Students dictionary:")
for student_id, info in students.items():
    print(f"{student_id}: {info}")