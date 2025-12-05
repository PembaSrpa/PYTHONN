"""
Standard Libraries in Python: Detailed Examples

Python comes with a rich set of standard libraries that provide modules and functions for many common tasks.
Below are some of the most important and commonly used standard libraries, along with practical, detailed examples.
"""

# -----------------------------
# IMPORTS
# -----------------------------
import os
import sys
import datetime
import math
import random
import json
from collections import Counter, defaultdict, namedtuple, deque
import re
from pathlib import Path

# -----------------------------
# 1. os – Operating System Interface
# -----------------------------
# Used for interacting with the operating system: file/directory operations, environment variables, and more.
print("1. os – Operating System Interface")
cwd = os.getcwd()
print(f"Current working directory: {cwd}")
print("Files and directories in cwd:", os.listdir(cwd))
# os.mkdir('test_dir')
# os.rename('test_dir', 'renamed_dir')
# os.rmdir('renamed_dir')
home_dir = os.environ.get('HOME', 'Not set')
print(f"HOME environment variable: {home_dir}")
print("-" * 50)

# -----------------------------
# 2. sys – Python Interpreter Interaction
# -----------------------------
print("2. sys – Python Interpreter Interaction")
print("Script name:", sys.argv[0])
print("Python version:", sys.version)
# sys.exit()
print("-" * 50)

# -----------------------------
# 3. datetime – Date and Time Manipulation
# -----------------------------
print("3. datetime – Date and Time Manipulation")
today = datetime.date.today()
print(f"Today's date: {today}")
now = datetime.datetime.now()
print(f"Current date and time: {now}")
yesterday = today - datetime.timedelta(days=1)
print(f"Yesterday was: {yesterday}")
print("-" * 50)

# -----------------------------
# 4. math – Mathematical Functions
# -----------------------------
print("4. math – Mathematical Functions")
print("Pi:", math.pi)
print("Cosine of 0:", math.cos(0))
print("Square root of 16:", math.sqrt(16))
print("Log base 10 of 100:", math.log10(100))
print("-" * 50)

# -----------------------------
# 5. random – Pseudorandom Number Generation
# -----------------------------
print("5. random – Pseudorandom Number Generation")
print("A random float between 0 and 1:", random.random())
print("A random integer between 1 and 10:", random.randint(1, 10))
choices = ['apple', 'banana', 'cherry']
print("Randomly chosen fruit:", random.choice(choices))
random.shuffle(choices)
print("Shuffled list:", choices)
print("-" * 50)

# -----------------------------
# 6. json – JSON Serialization
# -----------------------------
print("6. json – JSON Serialization")
data = {'name': 'Alice', 'age': 30, 'is_member': True}
json_str = json.dumps(data)
print("Serialized to JSON:", json_str)
parsed = json.loads(json_str)
print("Parsed from JSON:", parsed)
print("-" * 50)

# -----------------------------
# 7. collections – Specialized Container Data Types
# -----------------------------
print("7. collections – Specialized Container Data Types")
cnt = Counter(['a', 'b', 'a', 'c', 'b', 'b'])
print("Counter example:", cnt)
dd = defaultdict(int)
dd['unknown'] += 1
print("defaultdict example:", dict(dd))
Point = namedtuple('Point', 'x y')
pt = Point(2, 3)
print("namedtuple example:", pt, pt.x, pt.y)
dq = deque([1, 2, 3])
dq.appendleft(0)
print("deque example:", dq)
print("-" * 50)

# -----------------------------
# 8. re – Regular Expressions
# -----------------------------
print("8. re – Regular Expressions")
text = "My email is test@example.com."
matched = re.search(r'[\w.-]+@[\w.-]+', text)
if matched:
    print("Found email:", matched.group())
print("-" * 50)

# -----------------------------
# 9. pathlib – Object-oriented File System Paths (Python 3.4+)
# -----------------------------
print("9. pathlib – Object-oriented File System Paths (Python 3.4+)")
p = Path('.')
print("All .py files in cwd:", list(p.glob('*.py')))
print("Home directory:", Path.home())
print("-" * 50)

# -----------------------------
# 10. subprocess – Running Subprocesses
# -----------------------------
print("10. subprocess – Running Subprocesses")
# result = subprocess.run(['echo', 'Hello from subprocess'], capture_output=True, text=True)
# print("Subprocess output:", result.stdout.strip())
print("Subprocess example commented out for safety.")
print("-" * 50)

"""
Other Notable Standard Libraries:
- argparse: for parsing command-line options/arguments
- logging: flexible logging facility
- shutil: high-level file operations (copy, move, etc.)
- threading, multiprocessing: concurrent and parallel programming support
- http, urllib: HTTP and URL handling
- xml, csv: parsing XML/CSV files

See the official documentation for more on the Python Standard Library!
https://docs.python.org/3/library/
"""
