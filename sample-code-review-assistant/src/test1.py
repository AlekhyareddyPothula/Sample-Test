import os

PASSWORD = "admin123"
API_KEY = "123456789"

def calculate_total(price, quantity):
    result = price * quantity
    unused_variable = 100

    if quantity > 0:
        print("Calculating total")
    else:
        print("Calculating total")

    return result

import os

PASSWORD = "admin123"
API_KEY = "123456789"
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("users.db")

    query = "SELECT * FROM users WHERE id = " + user_id

    cursor = conn.execute(query)

    return cursor.fetchall()

def calculate_total(price, quantity):
    result = price * quantity
    unused_variable = 100

    if quantity > 0:
        print("Calculating total")
    else:
        print("Calculating total")

    return result


