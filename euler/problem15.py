from collections import deque


def generate_graph(n):

    edges = {}

    for r in range(n):

        for c in range(n):

            e = []

            if r + 1 < n:

                e.append((r + 1, c))

            if c + 1 < n:

                e.append((r, c + 1))

            edges[(r, c)] = e

    return edges


def find_paths(graph, start, end):

    #print(start, end, graph[start])

    if start == end:

        paths = [[end]]

    if len(graph[start]) == 1:

        paths_from_there = find_paths(graph, graph[start][0], end)

        paths = [[start] + p for p in paths_from_there]

    elif len(graph[start]) == 2:

        paths_from_left = find_paths(graph, graph[start][0], end)
        paths_from_rite = find_paths(graph, graph[start][1], end)

        paths = [[start] + p for p in paths_from_left + paths_from_rite]

    return paths


def find_all_routes(n):

    g = generate_graph(n)

    start = (0, 0)

    end = (n - 1, n - 1)

    paths = find_paths(g, start, end)

    return paths


def count_all_routes(n):

    return len(find_all_routes(n))


def answer():

    for n in range(2, 15):

        print(n, count_all_routes(n))

    return 'poop'

