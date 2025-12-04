# Loops in Python
colors = ('red', 'green', 'blue')
for color in colors:
    print(f"Color: {color}")
    
# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Looping over a string
text = "hello"
for char in text:
    print(f"Character: {char}")

# Looping over a dictionary
fruits = {'apple': 2, 'banana': 3, 'cherry': 5}
for fruit, quantity in fruits.items():
    print(f"{fruit}: {quantity}")

# Nested loops and flow control with conditions
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in matrix:
    for value in row:
        if value % 2 == 0:
            print(f"Even number: {value}")
        else:
            print(f"Odd number: {value}")