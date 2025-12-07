import pymysql
from config import MYSQL_CONFIG

def get_conn():
    return pymysql.connect(**MYSQL_CONFIG)


def create_user(name, email):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )
    conn.commit()
    conn.close()


def get_users():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return data


def get_user(uid):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (uid,))
    data = cursor.fetchone()
    conn.close()
    return data


def update_user(uid, name, email):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (name, email, uid)
    )
    conn.commit()
    conn.close()


def delete_user(uid):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (uid,))
    conn.commit()
    conn.close()
