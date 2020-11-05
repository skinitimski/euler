from math import sqrt

from euler.utils import factors


def triangle_numbers(limit):

    n = 1
    t = 0

    while n <= limit:

        t += n
        n += 1

        yield t


def all_factors(n):

    yield 1

    if n > 1:

        for f in factors(n):

            yield f


def divisors(n):

    for i in range(1, int(sqrt(n)) + 1):

        if n % i == 0:

            q = int(n / i)

            yield i

            if q != i:

                yield q


def first_triangle_number_with_more_than_n_divisors(n):

    for t in triangle_numbers(1000000):

        if len(list(divisors(t))) > n:

            return t


def answer():

    return first_triangle_number_with_more_than_n_divisors(500)

