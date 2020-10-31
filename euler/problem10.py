from itertools import islice


def primes_below_n(n):

    markers = [True] * n

    markers[0] = False
    markers[1] = False

    for (i, isprime) in enumerate(markers):

        if isprime:

            yield i

            for x in range(i * 2, n, i):

                markers[x] = False


def answer():

    return sum(primes_below_n(2000000))

