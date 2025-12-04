# Lambda functions are small anonymous functions defined with the lambda keyword.
# They are often used for short, throwaway functions.

# Basic lambda function example
add = lambda x, y: x + y  # noqa: E731
print("Sum using lambda:", add(2, 3))

# Lambda as an argument to higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# Filtering with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Sorting with lambda
points = [(2, 3), (4, 1), (1, 5), (3, 4)]
# Sort by y-coordinate
points_sorted = sorted(points, key=lambda point: point[1])
print("Points sorted by y-coordinate:", points_sorted)