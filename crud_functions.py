import sqlite3
import text_to_HW52


def initiate_db():
    connection = sqlite3.connect('db_zoj.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEST,
    price INT NIT NULL
    );
    ''')

    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   ('Апельсин', text_to_HW52.orange, text_to_HW52.orange_price))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   ('Брокколи', text_to_HW52.broccoli, text_to_HW52.broccoli_price))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   ('Марковка', text_to_HW52.carrot, text_to_HW52.carrot_price))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   ('Яблоко', text_to_HW52.apple, text_to_HW52.apple_price))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('db_zoj.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products
