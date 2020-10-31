from math import prod

from euler.utils import factors


def is_divisible_by_all(n, divisors):

    return all(n % d == 0 for d in divisors)


def smallest_divisible_by_divisors(n):

    divisors = list(range(2, n + 1))

    smallest = prod(divisors)

    for divisor in divisors:

        for f in factors(divisor):

            poop = int(smallest / f)

            if is_divisible_by_all(poop, divisors):

                smallest = poop

    return smallest


def main():

    for i in range(10, 21):

        print(i, smallest_divisible_by_divisors(i))

