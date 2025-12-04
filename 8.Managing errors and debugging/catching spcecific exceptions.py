# Example 1: Catching a ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")

# Example 2: Catching a ValueError when converting input to integer
try:
    n = int("abc")
except ValueError as e:
    print(f"Caught a ValueError: {e}")

# Example 3: Catching a FileNotFoundError when opening a file
try:
    with open("non_existent_file.txt") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"Caught a FileNotFoundError: {e}")

# Example 4: Catching a KeyError in a dictionary
try:
    d = {"a": 1}
    value = d["b"]
except KeyError as e:
    print(f"Caught a KeyError: {e}")

# Example 5: Catching an IndexError in a list
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"Caught an IndexError: {e}")

# Example 6: Catching an AttributeError
try:
    number = 42
    number.append(100)
except AttributeError as e:
    print(f"Caught an AttributeError: {e}")

# Example 7: Catching an ImportError
try:
    import non_existent_module
except ImportError as e:
    print(f"Caught an ImportError: {e}")

# Example 8: Catching a TypeError
try:
    s = "hello" + 5
except TypeError as e:
    print(f"Caught a TypeError: {e}")
