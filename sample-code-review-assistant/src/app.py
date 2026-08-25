"""
Sample app with INTENTIONAL code quality issues, for SonarQube testing only.
Do not use this code in production.
"""


import sqlite3
import os

# Hardcoded credentials (Blocker: python:S2068)
DB_PASSWORD = "SuperSecret123!"
API_KEY = "sk-test-1234567890abcdef"
AWS_SECRET_ACCESS_KEY = "AKIAABCDEFGHIJKLMNOP"


def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection via string concatenation (Blocker: python:S2077)
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    return result


def get_order(order_id):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    # SQL Injection via string concatenation (Blocker: python:S2077)
    query = "SELECT * FROM orders WHERE id = '" + order_id + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    return result


def divide(a, b):
    try:
        return a / b
    except:  # Bare except clause (Critical: python:S5754)
        pass


def run_command(cmd):
    # OS command injection (Blocker: python:S4721)
    os.system(cmd)


def unreachable_code_example():
    x = 10
    if False:
        print("this can never run")  # Dead/unreachable code (Critical: python:S1763)
    return None
