from importlib import import_module

from time import time_ns


problems_solved = range(1, 14)

problems = [(problem, import_module(f'euler.problem{problem}')) for problem in problems_solved]

answers = [
    233168,
    4613732,
    6857,
    (906609, 913, 993),
    232792560,
    25164150,
    104743,
    23514624000,
    31875000,
    142913828922,
    70600674,
    76576500,
    5537376230,
    837799,
    137846528820,
    1366,
    21124,
    1074,
    171,
    648,
    31626,
    871198282,
    4179871,
    2783915460,
    4782,
    983,
    -59231,
    669171001,
    9183,
    443839,
    73682,
    45228,
]


def main():

    for (number, module) in problems:

        print(f'Problem {number} ---------')

        start = time_ns()

        answer = module.answer()

        end = time_ns()

        assert answer == answers[number - 1], f'my answer, {answer}, is wrong'

        ms = (end - start) / 1000000

        assert ms < 1000, f'took too long! {ms}'

        print(f'Answer: {answer}')
        print(f'  Time: {ms}')

