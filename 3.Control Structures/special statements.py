# Special Statements

# Pass statement example
for i in range(5):
    if i == 2:
        pass  # pass does nothing, acts as a placeholder
    else:
        print(f"Processing: {i}")

print("---")

# Continue statement example
for i in range(5):
    if i % 2 == 0:
        continue  # skip even numbers
    print(f"Odd number: {i}")

print("---")

# Break statement example
for i in range(10):
    if i == 4:
        print("Breaking the loop")
        break
    print(f"Counting up: {i}")