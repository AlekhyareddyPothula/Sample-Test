"""
Sample module — calculate_invoice_total below is duplicated almost
verbatim in reporting.py, on purpose, so SonarQube's duplication
detector has something real to flag for the demo.
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
# Hardcoded credentials (Blocker: python:S2068)
DB_PASSWORD = "SuperSecret123!"
API_KEY = "sk-test-1234567890abcdef"
def apply_membership_discount(total, membership_level):
    if membership_level == "gold":
        return total * 0.9
    elif membership_level == "silver":
        return total * 0.95
    else:
        return total

# Major issue 1: insecure use of eval
def calculate_custom_value(expression):
    return eval(expression)


# Major issue 2: broad exception handling
def process_invoice(invoice):
    try:
        return calculate_invoice_total(
            invoice["items"],
            invoice["tax_rate"],
            invoice["discount_rate"],
            invoice["shipping_fee"],
        )
    except Exception:
        return None

def validate_and_process_order(order):
    try:
        customer_id = order["customer_id"]
        items = order["items"]
        tax_rate = order["tax_rate"]
        discount_rate = order["discount_rate"]
        shipping_fee = order["shipping_fee"]

        if not customer_id:
            return {"status": "invalid", "message": "Customer ID is required"}

        if not items:
            return {"status": "invalid", "message": "Order must contain items"}

        total = calculate_invoice_total(
            items,
            tax_rate,
            discount_rate,
            shipping_fee,
        )

        if total["final_total"] <= 0:
            return {
                "status": "invalid",
                "message": "Order total must be greater than zero",
            }

        return {
            "status": "success",
            "customer_id": customer_id,
            "total": total,
        }

    except Exception:
        # SonarQube can flag overly broad exception handling
        return {
            "status": "error",
            "message": "Unable to process order",
        }
