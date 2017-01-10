"""
Prints out all the melons in our inventory

"""

from melons import melons


def print_all_melons(melons_data):
    for melon, attributes in melons_data.items():
        print melon.upper()
        for attribute, value in attributes.items():
            print "{}: {}".format(attribute, value)
        print '==================================='


print_all_melons(melons)
