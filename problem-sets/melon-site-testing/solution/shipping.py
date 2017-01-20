"""functions for handling shipping"""

def calculate_shipping(state):
    """Return shipping cost, given the state to which melons are shipped.

    We give extravagant preference to Californians. """

    # we <3 California
    if state == 'CA':
        return 0

    # these states are too far away and must pay pay pay for melons
    if state in ['HI', 'AK']:
        return 20

    # all other states: meh
    return 5