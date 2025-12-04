# Example: Using try...except blocks for error handling

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That was not a valid integer. Please try again.")

