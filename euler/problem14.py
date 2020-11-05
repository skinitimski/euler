graph = {
}

def collatz(n):

    yield n

    while n > 1:

        if n % 2 == 0:

            r = int(n / 2)

        else:

            r = 3 * n + 1

        yield n


def collatz_length(n):

    if n == 1:

        return 1

    if n in graph:

        return graph[n]

    if n % 2 == 0:

        r = int(n / 2)

    else:

        r = 3 * n + 1

    # n -> r

    l = 1 + collatz_length(r)

    graph[n] = l

    return l


def longest_collatz_chain(n):

    return max([(x, collatz_length(x)) for x in range(1, n + 1)], key=lambda y: y[1])


def answer():

    return longest_collatz_chain(1000000)[0]


