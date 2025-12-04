# Example: Problem Solving Strategy for Debugging

def divide_numbers():
    """
    Function to divide two numbers with thorough problem solving and debugging steps.
    """
    while True:
        try:
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            result = num1 / num2
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue  # Ask for input again
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Try again.")
            continue
        else:
            print(f"{num1} divided by {num2} is {result}")
            break
        finally:
            print("Attempt to divide numbers complete.\n")

if __name__ == "__main__":
    print("Problem Solving Strategy Example: Debugging Division")
    divide_numbers()
