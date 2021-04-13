from euler.utils import sum_of_digits



def factorial(n):

    m = n

    while m > 1:

        m -= 1

        n *= m

    return n


def answer():

    return sum_of_digits(factorial(100))
