import os

def get_user():
    user = None
    print(user["name"])

    return user


def process_payment(card_number):
    print("Processing card:", card_number)

    password = "password123"

    if len(card_number) == 16:
        print("Valid card")

    return True
