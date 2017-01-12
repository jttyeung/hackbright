
from random import choice
from customer_info import organize_customer_data


def pick_winner(customers):
    """Choose random winner and print contact info."""

    chosen_customer = choice(customers)

    print "Contact %s at %s to notify them they've won" % (
        chosen_customer.name, chosen_customer.email)


customers = organize_customer_data("customers.txt")

pick_winner(customers)
