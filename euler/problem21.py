from euler.utils import divisors


def sum_of_proper_divisors(n):

    return sum(divisors(n)[:-1])


def sum_of_amicable_numbers_under(n):

    amicables = []

    spds = {i: sum_of_proper_divisors(i) for i in range(2, n + 1)}

    reverse_lookup = {v: k for k, v in spds.items()}

    for i in spds:

        if spds[i] in spds and spds[spds[i]] == i:

            amicables.append(i)

    amicables = [a for a in amicables if spds[a] != a]

    return sum(amicables)


def answer():

    return sum_of_amicable_numbers_under(10000)
