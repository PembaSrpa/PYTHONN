# CRUD Operations in MySQL using Python (mysql-connector-python)

import mysql.connector

def create_connection():
    """Create and return a new MySQL database connection."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_database"
    )
    return conn

def create_employee(name, age, department):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)",
        (name, age, department)
    )
    conn.commit()
    cur.close()
    conn.close()

def read_employees():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def update_employee(employee_id, name=None, age=None, department=None):
    conn = create_connection()
    cur = conn.cursor()
    # Build the dynamic update query based on provided fields
    fields = []
    values = []
    if name is not None:
        fields.append("name=%s")
        values.append(name)
    if age is not None:
        fields.append("age=%s")
        values.append(age)
    if department is not None:
        fields.append("department=%s")
        values.append(department)
    if not fields:
        cur.close()
        conn.close()
        return
    values.append(employee_id)
    query = f"UPDATE employees SET {', '.join(fields)} WHERE id=%s"
    cur.execute(query, tuple(values))
    conn.commit()
    cur.close()
    conn.close()

def delete_employee(employee_id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=%s", (employee_id,))
    conn.commit()
    cur.close()
    conn.close()

# --- Example Usage ---
if __name__ == "__main__":
    # Create
    create_employee("Frank", 33, "Marketing")
    # Read
    print("All employees:", read_employees())
    # Update
    update_employee(1, age=35, department="HR")  # Example: update employee with id=1
    # Delete
    delete_employee(2)  # Example: delete employee with id=2
    print("After update and delete:", read_employees())
