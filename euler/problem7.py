from itertools import islice

from euler.utils import factors


def is_prime(n):

    return len(list(factors(n))) == 1


def primes():

    i = 2

    while True:

        if is_prime(i):

            yield i

        i += 1


def nth_prime(n):

    return next(islice(primes(), n, None))


def answer():

    return nth_prime(10000) # next(islice(primes(), 10000, None))
