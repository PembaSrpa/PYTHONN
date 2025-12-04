# --- Reading from and writing to text files in Python ---

# Reading from a text file
with open("example.txt", "r") as file:
    contents = file.read()
    print("File Contents:")
    print(contents)

# Writing to a text file (this will overwrite existing content)
with open("output.txt", "w") as file:
    file.write("Hello, this is a new file.\n")
    file.write("Writing multiple lines is easy!\n")

# Appending to a text file
with open("output.txt", "a") as file:
    file.write("This line is appended at the end.\n")

# --- Common file handling modes ---
# 'r'   : Read (default)
# 'w'   : Write (overwrites file)
# 'a'   : Append (writes to end)
# 'x'   : Create (fails if exists)
# 'r+'  : Read & write

# --- File path handling with os module ---
import os

# Get absolute path
abs_path = os.path.abspath("example.txt")
print("Absolute Path:", abs_path)

# Check if a file exists
if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")

# Join directory and file name
directory = "my_folder"
filename = "file.txt"
full_path = os.path.join(directory, filename)
print("Full Path:", full_path)