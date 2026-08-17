"""
Sample module — the calculate_invoice_total function below is duplicated
almost verbatim in reporting.py, on purpose, so SonarQube's duplication
detector has something to flag for testing.
"""

def calculate_invoice_total(items, tax_rate, discount_rate, shipping_fee):
    subtotal = 0
    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 0)
        line_total = price * quantity
        subtotal += line_total
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
