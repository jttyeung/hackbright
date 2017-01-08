orig = ["apple", "berry", "cherry", "cherry"]


# def reverse_list_in_place(items):
#     """Reverse the input list `in place`.

#     Reverse the input list given, but do it "in place" --- that is,
#     do not create a new list and return it, but modify the original
#     list.

#     **Do not use** the python function `reversed()` or the method
#     `list.reverse()`.

#     For example::

#         >>> orig = [1, 2, 3]
#         >>> reverse_list_in_place(orig)
#         >>> orig
#         [3, 2, 1]

#         >>> orig = ["cookies", "love", "I"]
#         >>> reverse_list_in_place(orig)
#         >>> orig
#         ['I', 'love', 'cookies']
#     """

#     items_copy = items[::-1]
#     return items_copy
#     print id(items_copy)
#     items = items_copy
#     return items
#     print id(items)
# #     for item in items_copy:
# #       items
# #     return items


# # print orig
# print reverse_list_in_place(orig)
# # print orig


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """
    duplicates = items[:]  # show resulting duplicates only
    duplicates_set = set(duplicates)  # items with duplicates removed
    no_duplicates = list(duplicates_set)  # convert back to list

    for item in no_duplicates:
      position = duplicates.index(item)
      del duplicates[position]
    else:
      pass

    return sorted(duplicates)

print duplicates(orig)
print orig
