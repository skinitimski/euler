from importlib import import_module


problems_solved = [1, 2, 4, 5, 6]

problems = [(problem, import_module(f'euler.problem{problem}')) for problem in problems_solved]


def main():

    for (number, module) in problems:

        print(f'Problem {number} ---------')

        module.main()

