from math import pow

def sum_of_squares(n):

    return sum([x * x for x in range(1, n + 1)])


def square_of_sum(n):

    return int(pow(sum(range(1, n + 1)), 2))


def difference(n):

    return square_of_sum(n) - sum_of_squares(n)


def main():

    for i in range(10, 101, 10):

        print(i, difference(i))
