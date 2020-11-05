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


def factor_multiplicity(n):

    i = 1
    c = 0

    for factor in factors(n):

        if factor != i:

            yield i, c
            i = factor
            c = 0

        c += 1

    yield i, c


def divisors(n):

    d = [1]

    for p, m in factor_multiplicity(n):

        d += [x*p**k for k in range(1, m + 1) for x in d]

    return d


def first_triangle_number_with_more_than_n_divisors(n):

    for t in triangle_numbers(1000000):

        if len(list(divisors(t))) > n:

            return t


def answer():


    return first_triangle_number_with_more_than_n_divisors(500)

