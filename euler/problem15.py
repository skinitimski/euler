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


def count_paths(graph, lookup, start, end):

    if start in lookup:

        paths = lookup[start]

    elif start == end:

        paths = 1

    elif len(graph[start]) == 1:

        paths = count_paths(graph, lookup, graph[start][0], end)

    elif len(graph[start]) == 2:

        paths = count_paths(graph, lookup, graph[start][0], end) + count_paths(graph, lookup, graph[start][1], end)

    if start not in lookup:

        lookup[start] = paths

    return paths


def find_paths(graph, lookup, start, end):

    if start in lookup:

        return lookup[start]

    if start == end:

        paths = [[end]]

    elif len(graph[start]) == 1:

        paths_from_there = find_paths(graph, lookup, graph[start][0], end)

        paths = [[start] + p for p in paths_from_there]

    elif len(graph[start]) == 2:

        paths_from_left = find_paths(graph, lookup, graph[start][0], end)
        paths_from_rite = find_paths(graph, lookup, graph[start][1], end)

        paths = [[start] + p for p in paths_from_left + paths_from_rite]

    lookup[start] = paths

    return paths


def count_all_routes(n):

    graph = generate_graph(n + 1)

    lookup = {}

    start = (0, 0)

    end = (n, n)

    paths = count_paths(graph, lookup, start, end)

    return paths




def answer():

    return count_all_routes(20)

