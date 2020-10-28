def multiples(factor, limit):

    i = 1

    while i * factor < limit:

        yield i * factor
        i += 1


def sum_of_multiples(limit):

    deduped = set(multiples(3, limit)) | set(multiples(5, limit))

    return sum(deduped)




def main():

    print(sum_of_multiples(10))
    print(sum_of_multiples(1000))



