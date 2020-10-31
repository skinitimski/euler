
def is_triplet(a, b, c):

    return a * a + b * b == c * c



def answer():

    for a in range(1, 9999):

        for c in range(1, 9999):

            b = 1000 - a - c

            if is_triplet(a, b, c):

                return a * b * c


