count = int(raw_input('Enter how many primes to output: '))
prime_list = [2]  # list of primes always starts at 2 with a min count of 1


def primes(count):
    """ Takes a number and returns that number of primes counting up from 2 """

    prime_number = 3  # start checking for primes from 3
    divisor = prime_number / 2  # looking for divisors at half the number

    if count <= 0:  # check if count is at least 1
        return 'That is not a valid number. Enter 1 or greater.'

    while count > 1:  # tracks how many prime numbers to add to prime_list
        while divisor > 1:  # looking for divisors until smallest possible (2)
            if prime_number % divisor != 0:  # if the divisor is not a number it can be divided by
                divisor -= 1  # decrement the number by 1
            else:
                break  # when the prime_number has a divisor, break
        prime_list.append(prime_number)

        prime_number += 2  # check the next odd number
        count -= 1

    return prime_list

print primes(count)
# [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2]


# def primes(count):
#     prime_list = []
#     prime_number = 2
#     subtractor = 1

#     while count >= 2:
#         if prime_number % (prime_number - subtractor) == 0:
#             prime_list.append(prime_number)
#             prime_number += 1
#             count -= 1
#         else:
#             prime_number += 1
#             count -= 1
#             subtractor += 1

#     print prime_list



#     2, 3, 5, 7, 11, 13, 17, 19, 23, 29
#       1  2  2  4   2   4   2   4,  5

# if num cannot be divided by num - 1, num - 2, num - 3... num - num + 2:
#     then it is prime
# else it is


# # start at 1, keep counting by 1 and check if it's a prime
# n = 2
# n = 3   3 % (3-1) != 0  prime // 1 try
# n = 4   4 % (4-1) != 0
# n = 4   4 % (4-2) == 0
# n = 5   5 % (5-1) != 0
# n = 5   5 % (5-2) != 0
# n = 5   5 % (5-3) != 0  prime // 3 tries
# n = 6   6 % (6-1) != 0
# n = 6   6 % (6-2) != 0
# n = 6   6 % (6-3) == 0
# n = 7   7 % (7-1) != 0
# n = 7   7 % (7-2) != 0
# n = 7   7 % (7-3) != 0
# n = 7   7 % (7-4) != 0
# n = 7   7 % (7-5) != 0  prime // 5 tries

# n = 11  11 % (11-1) != 0
# n = 11  11 % (11-2) != 0
# n = 11  11 % (11-3) != 0
# n = 11  11 % (11-4) != 0
# n = 11  11 % (11-5) != 0
# n = 11  11 % (11-6) != 0
# n = 11  11 % (11-7) != 0
# n = 11  11 % (11-8) != 0
# n = 11  11 % (11-9) != 0    prime // 9 tries


# n starts with 2
# while count > 2,
#     n + 1
#     count - 1
