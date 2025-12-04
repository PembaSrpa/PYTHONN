# Example: Creating and using custom exceptions

# Define a custom exception by subclassing the built-in Exception class
class NegativeValueError(Exception):
    """Custom exception for negative values."""
    def __init__(self, value, message="Negative value is not allowed"):
        self.value = value
        self.message = message
        super().__init__(f"{message}: {value}")

def factorial(n):
    """Calculate factorial. Raise NegativeValueError for negative input."""
    if n < 0:
        raise NegativeValueError(n)
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

try:
    number = int(input("Enter a non-negative integer to compute its factorial: "))
    print(f"Factorial of {number} is {factorial(number)}")
except NegativeValueError as e:
    print(f"Custom exception caught: {e}")
except ValueError:
    print("Input must be an integer.")
