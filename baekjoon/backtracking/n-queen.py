import sys


def solution():
    input = sys.stdin.readline
    n = int(input())
    result = 0
    for start in range(n):
        queue = [[(0, start)]]
        while queue:
            locs = queue.pop()
            if len(locs) < n:
                for nc in range(n):
                    if is_possible(locs, nc):
                        queue.append(locs + [(locs[-1][0] + 1, nc)])
            else:
                result += 1
    print(result)


def is_possible(locs, nc):
    imp_cols = map(lambda x: x[1], locs)
    if nc in imp_cols:
        return False
    next_row = locs[-1][0] + 1
    imp_diag = map(lambda x: abs(next_row - x[0]) - abs(nc - x[1]), locs)
    if 0 in imp_diag:
        return False
    return True


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        solution()
