# Designing and Changing Databases and Tables in SQL (MySQL Context)

# 1. Creating a Database (MySQL)
# Syntax:
# CREATE DATABASE dbname;

# Example:
# CREATE DATABASE school;

# 2. Selecting a Database
# USE school;

# 3. Creating a Table
# Syntax:
# CREATE TABLE tablename (
#     column1 datatype constraints,
#     column2 datatype constraints,
#     ...
# );

# Example: Create a 'students' table
# CREATE TABLE students (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(100) NOT NULL,
#     age INT,
#     enrollment_date DATE
# );

# 4. Altering a Table (MySQL)

# a) Adding a new column
# ALTER TABLE students ADD COLUMN email VARCHAR(100);

# b) Modifying a column's datatype or constraints
# ALTER TABLE students MODIFY COLUMN age SMALLINT;

# c) Renaming a column
# ALTER TABLE students CHANGE name full_name VARCHAR(100);

# d) Dropping a column
# ALTER TABLE students DROP COLUMN email;

# 5. Dropping a Table or Database (MySQL)

# Drop a table:
# DROP TABLE students;

# Drop a database:
# DROP DATABASE school;

# 6. Example Workflow (MySQL)

# -- Create a database and table
# CREATE DATABASE company;
# USE company;
# CREATE TABLE employees (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(100) NOT NULL,
#     department VARCHAR(100),
#     hire_date DATE
# );

# -- Change the employees table
# ALTER TABLE employees ADD COLUMN salary DECIMAL(10,2);

# -- Rename column (MySQL)
# ALTER TABLE employees CHANGE department dept VARCHAR(100);

# -- Drop column
# ALTER TABLE employees DROP COLUMN hire_date;


