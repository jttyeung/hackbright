
# Part 1: Fundamental operations on lists
# ---------------------------------------
#
# The fundamental operations on lists in Python are those that are part of the
# language syntax and/or cannot be implemented in terms of other list operations:
#
#     * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
#     * List indexing (some_list[index])
#     * List indexing assignment (some_list[index] = value)
#     * List slicing (some_list[start:end])
#     * List slicing assignment (some_list[start:end] = another_list)
#     * List index deletion (del some_list[index])
#     * List slicing deletion (del some_list[start:end])
#
# In this section you will implement functions that each use just one of the above
# operations. The docstring of each function describes what it should do.
#
# DO NOT USE ANY OF THE BUILT IN LIST METHODS, OR len(l)


def head(input_list):
    """
    Return the first element of the input list.

    For example:

    >>> head(['Jan', 'Feb', 'Mar'])
    'Jan'

    """

    return input_list[0]


def tail(input_list):
    """
    Return all elements of the input list except the first.

    For example:

    >>> tail(['Jan', 'Feb', 'Mar'])
    ['Feb', 'Mar']

    """

    return input_list[1:]


def last(input_list):
    """
    Return the last element of the input list.

    For example:

    >>> last(['Jan', 'Feb', 'Mar'])
    'Mar'

    """

    return input_list[-1]


def init(input_list):
    """
    Return all elements of the input list except the last.

    For example:

    >>> init(['Jan', 'Feb', 'Mar'])
    ['Jan', 'Feb']

    """

    return input_list[:-1]


##############################################################################
# Do yourself a favor and get a short code review here.
# You can also get reviewed by a neighbor who has been reviewed.


def first_three(input_list):
    """
    Return the first three elements of the input list.

    For example:

    >>> first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['Jan', 'Feb', 'Mar']

    """

    return input_list[:3]


def last_five(input_list):
    """
    Return the last five elements of the input list.

    For example:

    >>> last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [15, 18, 21, 24, 27]

    """

    return input_list[-5:]


def middle(input_list):
    """
    Return all elements of the input list except the first two and the last two.

    For example:

    >>> middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15, 18, 21]

    """

    return input_list[2:-2]


def inner_four(input_list):
    """
    Return the third, fourth, fifth, and sixth elements of the input list.

    For example:

    >>> inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15]

    """

    return input_list[2:6]


def inner_four_end(input_list):
    """
    Return the sixth, fifth, fourth, and third elements from the end of the
    list, in that order.

    For example:

    >>> inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [12, 15, 18, 21]

    """

    return input_list[-6:-2]


def replace_head(input_list):
    """
    Replace the head of the input list with the value 42 and
    return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_head(multiples)
    >>> multiples == [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    True

    """

    input_list[0] = 42


def replace_third_and_last(input_list):
    """
    Replace the third and last elements of the input list with the value 37
    and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_third_and_last(multiples)
    >>> multiples == [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]
    True

    """

    input_list[2], input_list[-1] = 37, 37


def replace_middle(input_list):
    """
    Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements. Return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_middle(multiples)
    >>> multiples == [0, 3, 42, 37, 24, 27]
    True

    """

    input_list[2:-2] = [42, 37]


def delete_third_and_seventh(input_list):
    """
    Remove the third and seventh elements of the input list and return
    nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_third_and_seventh(notes)
    >>> notes == ['Do', 'Re', 'Fa', 'So', 'La', 'Do']
    True

    """

    del input_list[2]
    del input_list[5]


def delete_middle(input_list):
    """
    Remove all elements from the input list except for the first two and the
    last two. Return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_middle(notes)
    >>> notes == ['Do', 'Re', 'Ti', 'Do']
    True

    """

    input_list[2:-2] = []


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#
# Please ask for a code review from an instructor/TA before proceeding.


if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"
