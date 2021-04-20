from math import sqrt

def sum_of_digits(n):

    return sum(int(i) for i in str(n))


def factors(n):

    j = 2

    while n > 1:

        for i in range(j, int(sqrt(n)) + 1):

            if n % i == 0:

                n = int(n / i)
                j = i

                yield i
                break

        else:

            if n > 1:

                yield n
                break


def divisors(n):

    d = [1]

    for p, m in factor_multiplicity(n):

        d += [x*p**k for k in range(1, m + 1) for x in d]

    return d


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


