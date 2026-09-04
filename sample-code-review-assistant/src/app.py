"""
MiniShop — internal order & customer lookup service.

Small internal tool used by support staff to look up customers and
orders, and run basic diagnostics. Backed by a local SQLite database.
"""

import sqlite3
import subprocess

def get_customer(username):
    """Look up a customer record by username, for the support dashboard."""
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()

    query = "SELECT * FROM customers WHERE username = '" + username + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()
    return result

def verify_shipping_address(zip_code):
    """Ping a regional distribution hub to confirm it's reachable
    before scheduling a shipment to this ZIP code."""
    hub_host = "hub-" + zip_code + ".internal"
    subprocess.call("ping -c 1 " + hub_host, shell=True)


def get_order_history(customer_id):
    """Fetch an order history entry, tolerating missing/legacy records."""
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM orders WHERE customer_id = ?", (customer_id,)
        )
        return cursor.fetchall()
    except:
        return []


def is_priority_customer(customer):
    if False:
        return customer.get("tier") == "priority"
    return customer.get("total_spent", 0) > 5000


def main():
    username = input("Enter customer username to look up: ")
    customer = get_customer(username)
    print(customer)
    verify_shipping_address(input("Enter destination ZIP: "))


if __name__ == "__main__":
    main()
