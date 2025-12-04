# Functions can have default values for arguments. If a value isn't provided by the caller, the default is used.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")            # Uses default greeting
greet("Bob", "Hi")        # Overrides default greeting

# Keyword arguments allow you to specify which parameter gets which value, regardless of their position.
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Rex")           # Positional arguments
describe_pet(name="Mittens", animal="cat")  # Keyword arguments, order doesn't matter

# You can mix positional and keyword arguments, but positional must come first.
def order(item, size="medium", quantity=1):
    print(f"Order: {quantity} {size} {item}(s)")

order("coffee")                              # Uses default size and quantity
order("sandwich", quantity=2)                # Override quantity
order(item="tea", size="large", quantity=3)  # All keyword arguments
