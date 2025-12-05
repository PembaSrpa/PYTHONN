# Filtering Data with the WHERE Clause in MySQL

# The WHERE clause in MySQL lets you filter the rows returned by a SELECT query according to specified conditions.

# 1. Basic Usage Example:

# Select all employees older than 30
"""
SELECT * FROM employees
WHERE age > 30;
"""

# 2. Multiple Conditions

# You can combine conditions using AND, OR, and parentheses for grouping.
"""
SELECT * FROM employees
WHERE department = 'IT' AND age >= 25;
"""

# 3. Pattern Matching with LIKE

# Find employees whose name starts with 'A'
"""
SELECT * FROM employees
WHERE name LIKE 'A%';
"""

# 4. Filtering for NULL Values

# Select employees where email is not provided (NULL email)
"""
SELECT * FROM employees
WHERE email IS NULL;
"""

# 5. Using IN and BETWEEN

# Select employees in specific departments
"""
SELECT * FROM employees
WHERE department IN ('IT', 'HR');
"""

# Select employees hired between two dates
"""
SELECT * FROM employees
WHERE hire_date BETWEEN '2022-01-01' AND '2022-12-31';
"""

# 6. Negation with NOT

# Exclude a department
"""
SELECT * FROM employees
WHERE NOT department = 'Sales';
"""

# TIP: In MySQL, WHERE appears after FROM (and JOIN clauses) but before GROUP BY, ORDER BY, and LIMIT.

# MySQL Python Example using mysql-connector-python

import mysql.connector

# Establish connection to MySQL (replace with your MySQL settings)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cur = conn.cursor()

# Example: Create sample table and insert data (executed only once for setup)
cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        age INT,
        department VARCHAR(100)
    )
""")

cur.execute("TRUNCATE TABLE employees")  # Clear table before inserting
cur.executemany(
    "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)",
    [
        ("Alice", 34, "IT"),
        ("Bob", 28, "HR"),
        ("Cathy", 41, "Sales"),
        ("David", 25, "IT"),
        ("Ella", 29, "Marketing"),
    ]
)
conn.commit()

# Fetch all employees from IT older than 30
cur.execute("SELECT * FROM employees WHERE department = %s AND age > %s", ("IT", 30))
rows = cur.fetchall()
print("IT employees older than 30:", rows)
cur.close()
conn.close()
