import sys


def solution():
    input = sys.stdin.readline
    n, m = map(int, input().strip().split())
    graph = range(1, n + 1)
    result = []
    for start in range(1, n + 1):
        queue = [[start]]
        while queue:
            path = queue.pop()
            if len(path) < m:
                for n in reversed(graph):
                    queue.append(path + [n])
            else:
                result.append(path)
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
