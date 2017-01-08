"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

quit = False

while quit is False:
    read_expression = raw_input()

    if read_expression != 'q':
        read_expression = read_expression.split(' ')

        operator = read_expression[0]
        string_nums = read_expression[1:]
        nums = map(int, string_nums)

        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide,
            'square': square,
            'cube': cube,
            'power': power,
            'mod': mod
        }

        if operator in operations:
            print operations[operator](*nums)
        else:
            print 'Sorry, try another operator.'

    else:
        quit = True
