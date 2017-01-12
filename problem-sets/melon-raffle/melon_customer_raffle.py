from random import choice


class Customer(object):
    """A customer at Ubermelon."""

    def __init__(self, name, email, street, city, zipcode):
        self.name = name
        self.email = email
        self.street = street
        self.city = city
        self.zipcode = zipcode


def organize_customer_data(customer_file_path):
    """Read customer file and return list of customer objects.

    Read file at customer_file_path and create a customer object containing
        customer information.

    """

    customers = []

    customer_file = open(customer_file_path)

    # Process a file like:
    #
    #   customer-name | email | street | city | zipcode

    for line in customer_file:
        customer_data = line.strip().split("|")
        name, email, street, city, zipcode = customer_data

        new_customer = Customer(name, email, street, city, zipcode)
        customers.append(new_customer)

    return customers


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)

    print "Contact {name} at {email} to notify them they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )


customers = organize_customer_data("customers.txt")

pick_winner(customers)
