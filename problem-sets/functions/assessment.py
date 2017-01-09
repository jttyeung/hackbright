"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def is_hometown(townname):
    """
    Returns True if townname matches hometown, otherwise returns False.

    Example:
        >>> is_hometown('San Francisco')
        True

        >>> is_hometown('Boston')
        False

    """
    if townname.lower() == 'san francisco':
        return True
    else:
        return False


#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def concatenate_name(firstname, lastname):
    """
    Returns concatenated first name and last name in a string, separated by a space.

    Example:
        >>> concatenate_name('Joanne','Yeung')
        'Joanne Yeung'
    """
    return firstname + ' ' + lastname

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def greeting(hometown, firstname, lastname):
    """
    Greets individual by first and last name and evaluates if their hometown matches yours.

    Examples:
        >>> greeting('Paris', 'Michele', 'Leon')
        'Hi Michele Leon, where are you from?'

        >>> greeting('San Francisco', 'Patrick', 'Brady')
        "Hi, Patrick Brady, we're from the same place!"
    """
    fullname = concatenate_name(firstname, lastname)

    if is_hometown(hometown):
        return 'Hi, {}, we\'re from the same place!'.format(fullname)
    else:
        return 'Hi {}, where are you from?'.format(fullname)

    # Why does the second test fail (Patrick Brady) when the greeting response is
    # wrapped in single quotes instead of double?



###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if fruit.lower() in ('strawberry', 'cherry', 'blackberry'):
        return True
    else:
        return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit):
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    return lst + [num]



# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(item_price, state, tax=.05):
    """
    Calculates total cost of item including state tax rates.
    """

    item_price_including_tax = float(item_price * (1 + tax))
    total_cost = None

    if state == 'CA':
        total_cost = item_price_including_tax * 1.03

    elif state == 'PA':
        total_cost = item_price_including_tax + 2

    elif state == 'MA':
        if item_price < 100:
            total_cost = item_price_including_tax + 1
        else:
            total_cost = item_price_including_tax + 3

    else:
        if tax == 0:
            return item_price
        else:
            total_cost = item_price_including_tax

    return float("{0:.1f}".format(total_cost))


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def create_list(*args):
    """
    Creates and returns a list which adds each given argument to the list
    in the order it was given.

    Examples:
        >>> create_list('ask', 'me', 'anything', 9)
        ['ask', 'me', 'anything', 9]

        >>> create_list(['hello'], 'four', 10, 1, 3)
        [['hello'], 'four', 10, 1, 3]
    """

    lst = []
    for arg in args:
        lst.append(arg)
    return lst


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def outer_function(word):
    """
    Returns the original word given and the word listed 3 times.

    Example:
        >>> outer_function("Balloonicorn")
        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')
    """

    def inner_function():
        return word * 3
    return word, inner_function()



# time spent: ~ 1 hour 30 minutes


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
