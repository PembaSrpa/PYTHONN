import pymysql
from pymysql.cursors import DictCursor
from config import MYSQL_CONFIG

def get_conn():
    return pymysql.connect(**MYSQL_CONFIG)

def init_db():
    # First, connect without database to create it if needed
    config_no_db = {k: v for k, v in MYSQL_CONFIG.items() if k != 'database'}
    conn = pymysql.connect(**config_no_db)
    cur = conn.cursor()
    
    # Create database if it doesn't exist
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_CONFIG['database']}")
    conn.commit()
    conn.close()
    
    # Now connect to the database and create table
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255),
        price VARCHAR(50),
        stock VARCHAR(50),
        url TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_product(title, price, stock, url):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO products (title, price, stock, url)
        VALUES (%s, %s, %s, %s)
    """, (title, price, stock, url))
    conn.commit()
    conn.close()

def fetch_all():
    conn = get_conn()
    cur = conn.cursor(DictCursor)
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    conn.close()
    return data    