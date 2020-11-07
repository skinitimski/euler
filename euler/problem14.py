from time import time_ns

graph = {}

def collatz(n):

    yield n

    while n > 1:

        if n % 2 == 0:

            r = int(n / 2)

        else:

            r = 3 * n + 1

        yield n


# winner?
#
# this seems to be faster than several other internet solutions...
# faster than https://stackoverflow.com/a/29514541 for first 1000000
# faster than https://stackoverflow.com/a/59807698
# faster than https://stackoverflow.com/a/46145956
#
# apparently faster than collatz_length2() for solving the first 1000000 than a given number
def collatz_length(n):

    if n == 1:

        return 1

    if n in graph:

        return graph[n]

    if n % 2 == 0:

        r = int(n / 2)

    else:

        r = 3 * n + 1

    l = 1 + collatz_length(r)

    graph[n] = l

    return l


# apparently faster than collatz_length() for solving a given number than the first 1000000
# faster than https://stackoverflow.com/a/29514541
def collatz_length2(n):

    l = 0
    c = n

    while c > 1:

        if c in graph:

            l += graph[c]

            break

        if c % 2 == 0:

            c = int(c / 2)

        else:

            c = 3 * c + 1

        l += 1

    graph[n] = l

    return l



def longest_collatz_chain(n):

    return max([(x, collatz_length2(x)) for x in range(1, n + 1)], key=lambda y: y[1])


def answer():

    return longest_collatz_chain(1000000)[0]


def stress():

    n = 10

    for case in ['collatz_length', 'collatz_length2']:

        times = []

        for i in range(n):

            f = globals()[case]

            start = time_ns()

            for r in range(1, 1000001):

                f(r)

            #f(837799)

            end = time_ns()

            graph.clear()

            ms = (end - start) / 1000000

            times.append(ms)

        avg = sum(times) / len(times)

        print(f'Case: {case}')
        print(f' Avg: {avg}')



