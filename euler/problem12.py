from math import sqrt

from euler.utils import divisors


def triangle_numbers(limit):

    n = 1
    t = 0

    while n <= limit:

        t += n
        n += 1

        yield t


def first_triangle_number_with_more_than_n_divisors(n):

    for t in triangle_numbers(1000000):

        if len(list(divisors(t))) > n:

            return t


def answer():


    return first_triangle_number_with_more_than_n_divisors(500)

