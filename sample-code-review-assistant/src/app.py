"""
Simple order-processing service.
Demo application used to showcase the Automated Code Review Assistant.
"""

import json


class OrderError(ValueError):
    """Raised when an order payload is invalid."""


def load_order(raw_json):
    """Parse and validate an incoming order payload."""
    try:
        order = json.loads(raw_json)
    except json.JSONDecodeError as e:
        raise OrderError(f"Invalid order JSON: {e}") from e

    if "items" not in order or not isinstance(order["items"], list):
        raise OrderError("Order must contain an 'items' list")

    return order


def calculate_order_total(order):
    """Return the total price for an order, before tax/shipping."""
    total = 0.0
    for item in order["items"]:
        price = item.get("price", 0)
        quantity = item.get("quantity", 1)
        total += price * quantity
    return round(total, 2)


def apply_discount(total, discount_code):
    """Apply a simple discount code to an order total."""
    discounts = {
        "SAVE10": 0.10,
        "SAVE20": 0.20,
    }
    rate = discounts.get(discount_code, 0)
    return round(total * (1 - rate), 2)


def process_order(raw_json, discount_code=None):
    """End-to-end processing of a single order payload."""
    order = load_order(raw_json)
    total = calculate_order_total(order)

    if discount_code:
        total = apply_discount(total, discount_code)

    return {
        "order_id": order.get("order_id"),
        "total": total,
        "item_count": len(order["items"]),
    }
