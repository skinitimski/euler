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


