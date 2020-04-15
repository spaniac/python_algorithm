import sys


def solution():
    input = sys.stdin.readline
    n, m = map(int, input().strip().split())
    graph = {i: list({a for a in range(1, n + 1)} - {i}) for i in range(1, n + 1)}
    result = []
    for start in range(1, n + 1):
        queue = [([start], start)]
        while queue:
            path, current = queue.pop()
            if len(path) < m:
                for n in set(graph[current]) - set(path):
                    queue.append((path + [n], n))
            else:
                result.append(path)
    result.sort(key=lambda x: tuple(a for a in x))
    for r in result:
        line = ''
        for e in r:
            line += str(e) + ' '
        print(line.strip())


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        solution()
