# def say_hi(name):
#     """
#     Takes a string name and prints 'Hi' + name
#     """
#     try:
#         name.isalpha()
#         print 'Hi', name
#     except ValueError:
#         print 'Please enter a valid name'

# say_hi(9)


def repeat_string(string, integer):
    """
    Takes a string and integer and prints the string (integer) number of times.
    """
    print string * integer


repeat_string('alkdja aa', 5)
