def is_palindrome(number):

    string = f'{number}'

    half = int(len(string) / 2)

    first_half = string[slice(0, half, 1)]

    second_half = string[-1:-(half+1):-1]

    return first_half == second_half


def n_digit_numbers(digits):

    return [d for d in range(10 ** (digits - 1), 10 ** digits)]


def products_of_n_digit_numbers(digits):

    return [(x * y, x, y) for x in n_digit_numbers(digits) for y in n_digit_numbers(digits)]


def palindromes_in_products(digits):

    return [x for x in products_of_n_digit_numbers(digits) if is_palindrome(x[0])]


def largest_palindrome(digits):

    key = lambda s: s[0]

    return max(palindromes_in_products(digits), key=key)


def main():

    print(largest_palindrome(3))



