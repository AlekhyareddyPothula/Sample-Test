"""
Sample app with INTENTIONAL code quality issues — for SonarQube demo purposes only.
Do not use this code in production.
"""

import sqlite3
import os

# Hardcoded credentials (Blocker: python:S2068)
DB_PASSWORD = "SuperSecret123!"
API_KEY = "sk-test-1234567890abcdef"
AWS_SECRET_ACCESS_KEY = "AKIAABCDEFGHIJKLMNOP"

import subprocess

def run_ping(host):
    # Intentionally vulnerable: OS command injection
    command = "ping -c 1 " + host
    subprocess.call(command, shell=True)
    
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
        print("this can never run")  # Dead/unreachable code (Critical: python:S5797)
    return None


# --------------------------------------------------------------------
# NOTE FOR THE LIVE DEMO:
# Add a new function below this line during the demo (e.g. another
# SQL-injection-style query, or a bare except) to show SonarQube
# catching a brand-new issue on a fresh push, in real time.
# See the suggested snippet in the project notes / chat history.
# --------------------------------------------------------------------
