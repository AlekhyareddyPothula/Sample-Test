"""
Sample module — calculate_invoice_total_for_report below is copy-pasted
from billing.py's calculate_invoice_total, on purpose, to trigger
SonarQube's duplication detector for the demo.
"""


def calculate_invoice_total_for_report(items, tax_rate, discount_rate, shipping_fee):
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


def generate_report(orders):
    unused_flag = True  # Unused variable (Minor: python:S1481)

    report_lines = []
    for order in orders:
        # High cyclomatic complexity on purpose (Critical: python:S3776)
        if order["status"] == "paid":
            if order["region"] == "US":
                if order["amount"] > 1000:
                    report_lines.append(f"Large US order: {order['id']}")
                else:
                    report_lines.append(f"US order: {order['id']}")
            elif order["region"] == "EU":
                if order["amount"] > 1000:
                    report_lines.append(f"Large EU order: {order['id']}")
                else:
                    report_lines.append(f"EU order: {order['id']}")
            else:
                report_lines.append(f"Other region order: {order['id']}")
        elif order["status"] == "pending":
            report_lines.append(f"Pending order: {order['id']}")
        else:
            report_lines.append(f"Unknown status order: {order['id']}")

    return report_lines
