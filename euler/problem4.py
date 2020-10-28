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

    print(is_palindrome(101))
    print(is_palindrome(1001))
    print(is_palindrome(2001))
    print(is_palindrome('penis'))
    print(is_palindrome('foobarraboof'))
    print(is_palindrome('foobaraboof'))

    print(n_digit_numbers(1))
    print(n_digit_numbers(2))
    print(n_digit_numbers(3))

    print(palindromes_in_products(3))

    print(largest_palindrome(3))



