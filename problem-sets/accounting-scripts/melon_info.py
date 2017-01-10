"""
Prints out all the melons in our inventory
"""

from melons import melons


# def print_melon(melon_data):
#     """
#     Returns the charateristics and price of the melon.
#     """
#     have_or_have_not = 'have'
#     if melons[melon_name]['seedless']:
#         have_or_have_not = 'do not have'

#     price = melons[melon_name]['price']
#     flesh_color = melons[melon_name]['flesh_color']
#     weight = melons[melon_name]['weight']
#     rind_color = melons[melon_name]['rind_color']

#     print "{}s {} seeds, have {} flesh, have a {} rind, weigh {}, and are
#     ${:.2f}".format(melon_name, have_or_have_not, flesh_color, rind_color,
#     weight, price)


# for melon in melons:
#     print_melon(melon)


def print_melons(melon_data):
    """
    Returns the charateristics and price of the melon.
    """
    for melon, attributes in melon_data.items():
        print
        print melon
        for attribute, value in attributes.items():
            print "{}: {}".format(attribute, value)

print_melons(melons)
