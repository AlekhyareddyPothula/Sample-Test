"""
Sample module intentionally containing SonarQube issues for testing.

DO NOT use this code in production.
"""


def calculate_invoice_total(items, tax_rate, discount_rate, shipping_fee):
    subtotal = 0

    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 0)
        line_total = price * quantity
        subtotal += line_total

    discount_amount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount_amount

    tax_amount = discounted_subtotal * tax_rate
    total_before_shipping = discounted_subtotal + tax_amount

    final_total = total_before_shipping + shipping_fee

    if final_total < 0:
        final_total = 0

    return {
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "shipping_fee": shipping_fee,
        "final_total": final_total,
    }


def apply_membership_discount(total, membership_level):
    if membership_level == "gold":
        return total * 0.9
    elif membership_level == "silver":
        return total * 0.95
    else:
        return total


# 1. High cognitive complexity / deeply nested conditions
def process_customer(customer):
    if customer:
        if customer.get("active"):
            if customer.get("verified"):
                if customer.get("country") == "IN":
                    if customer.get("age", 0) >= 18:
                        if customer.get("balance", 0) > 0:
                            if customer.get("subscription"):
                                return "premium"
                            else:
                                return "standard"
                        else:
                            return "no_balance"
                    else:
                        return "underage"
                else:
                    return "foreign"
            else:
                return "unverified"
        else:
            return "inactive"

    return "invalid"


# 2. Duplicate literal strings
def validate_user(user):
    errors = []

    if not user.get("name"):
        errors.append("User information is required")

    if not user.get("email"):
        errors.append("User information is required")

    if not user.get("phone"):
        errors.append("User information is required")

    return errors


# 3. Unused variables
def calculate_report(data):
    total_records = len(data)
    unused_value = 12345
    another_unused_value = "temporary"

    result = []
    for record in data:
        result.append(record)

    return result


# 4. Magic numbers
def calculate_bonus(salary, years):
    if years > 5:
        return salary * 1.25

    if years > 3:
        return salary * 1.15

    if years > 1:
        return salary * 1.05

    return salary


# 5. Very long method / multiple responsibilities
def process_order(order):
    customer = order.get("customer")
    items = order.get("items", [])
    discount = order.get("discount", 0)
    shipping = order.get("shipping", 0)

    subtotal = 0

    for item in items:
        subtotal += item.get("price", 0) * item.get("quantity", 0)

    discounted = subtotal - (subtotal * discount)
    tax = discounted * 0.18
    total = discounted + tax + shipping

    if customer:
        print("Customer:", customer.get("name"))
        print("Email:", customer.get("email"))

    if total > 10000:
        print("Large order")

    if total > 50000:
        print("Very large order")

    if not items:
        print("Order has no items")

    if total < 0:
        total = 0

    return total


# 6. Bare/broad exception handling
def load_customer(customer_id):
    try:
        customer = get_customer_from_database(customer_id)
        return customer
    except Exception:
        return None


# 7. Function with too many branches
def get_status(code):
    if code == 200:
        return "success"
    elif code == 201:
        return "created"
    elif code == 202:
        return "accepted"
    elif code == 204:
        return "no_content"
    elif code == 400:
        return "bad_request"
    elif code == 401:
        return "unauthorized"
    elif code == 403:
        return "forbidden"
    elif code == 404:
        return "not_found"
    elif code == 500:
        return "server_error"
    elif code == 502:
        return "bad_gateway"
    elif code == 503:
        return "service_unavailable"
    else:
        return "unknown"


# 8. Hardcoded credential / secret for security-rule testing
DATABASE_USERNAME = "admin"
DATABASE_PASSWORD = "admin123"
API_KEY = "test-secret-api-key-123456"


# 9. SQL injection-style issue for security testing
def find_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return execute_query(query)


# 10. Command injection-style issue
import os


def run_command(user_input):
    os.system("echo " + user_input)


# 11. TODO / FIXME comments
def unfinished_feature():
    # TODO: implement proper validation
    # FIXME: remove this temporary workaround
    return True


# 12. Mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return items


# 13. Dead/unreachable code
def calculate_value(value):
    if value > 0:
        return value

    return 0

    print("This code can never execute")


# 14. Duplicate code similar to calculate_invoice_total
def calculate_invoice_total_duplicate(
    items, tax_rate, discount_rate, shipping_fee
):
    subtotal = 0

    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 0)
        line_total = price * quantity
        subtotal += line_total

    discount_amount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount_amount

    tax_amount = discounted_subtotal * tax_rate
    total_before_shipping = discounted_subtotal + tax_amount

    final_total = total_before_shipping + shipping_fee

    if final_total < 0:
        final_total = 0

    return {
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "shipping_fee": shipping_fee,
        "final_total": final_total,
    }


def get_customer_from_database(customer_id):
    return {"id": customer_id}


def execute_query(query):
    return query
