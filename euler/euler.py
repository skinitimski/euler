from importlib import import_module

from time import time_ns


problems_solved = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
    142913828922
]


def main():

    for (number, module) in problems:

        print(f'Problem {number} ---------')

        start = time_ns()

        answer = module.answer()

        end = time_ns()

        assert answer == answers[number - 1], f'my answer, {answer}, is wrong'

        length = (end - start) / 1000000

        print(f'Answer: {answer}')
        print(f'  Time: {length}')

