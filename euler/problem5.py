def smallest_divisible_by_divisors(n):

    i = 1

    while True:

        if all([True if i % divisor == 0 else False for divisor in range(1, n + 1]):

            break

        i += 1

        if i % 100000 == 0:

            print('.', end='')

    return i

def main():

    # the results side-by-side are surprising!

    for i in range(10, 21):

        print(i, smallest_divisible_by_divisors(i))
