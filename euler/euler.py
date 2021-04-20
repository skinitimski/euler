from importlib import import_module

from time import time_ns


problems_solved = range(1, 23)

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
    142913828922, # 10
    70600674,
    76576500,
    5537376230,
    837799,
    137846528820, # 15
    1366,
    21124,
    1074,
    171,
    648, # 20
    31626,
    871198282,
    4179871,
    2783915460,
    4782, # 25
    983,
    -59231,
    669171001,
    9183,
    443839,
    73682,
    45228,
]

def solve():

    for (number, module) in problems:

        print(f'--- Problem: {number} ------------------')

        start = time_ns()

        answer = module.answer()

        end = time_ns()

        right_answer = answers[number - 1]

        assert answer == right_answer, f'my answer, {answer}, is wrong. The right answer is {right_answer}'

        ms = (end - start) / 1000000

        assert ms < 2000, f'took too long! {ms}'

        print(f'     Answer: {answer}')
        print(f'  Time (ms): {ms}')


def main():

    solve()
    #problems[13][1].stress()
