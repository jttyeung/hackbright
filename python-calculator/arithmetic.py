def add(*args):
    result = 0
    for i in args:
        result += i
    return result


def subtract(args):
    result = 0
    for i in args:
        result -= i
    return result


def multiply(args):
    result = 0
    for i in args:
        result *= i
    return result


def divide(args):
    # Need to turn at least argument to float for division to
    # not be integer division
    result = 0
    for i in args:
        result /= float(i)
    return result


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
