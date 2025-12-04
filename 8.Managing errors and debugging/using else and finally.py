# Example: Using else and finally in try...except blocks

try:
    number = int(input("Enter a number greater than zero: "))
    reciprocal = 1 / number
except ValueError:
    print("You did not enter a valid integer.")
except ZeroDivisionError:
    print("Zero is not allowed.")
else:
    print(f"The reciprocal of {number} is {reciprocal}")
finally:
    print("Execution of try...except...else...finally block is complete.")
