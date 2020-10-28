def fibonacci(limit):

    previous = 0
    current  = 1

    while current < limit:

        n = previous + current

        previous = current
        current  = n

        yield n


def sum_of_even_fibonacci(limit):

    return sum(t for t in fibonacci(limit) if t % 2 == 0)


def main():

    print(sum_of_even_fibonacci(4000000))





