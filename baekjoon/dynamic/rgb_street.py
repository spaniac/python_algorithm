import sys


def solution():
    input = sys.stdin.readline
    h = int(input())
    costs = list(map(int, input().strip().split()))
    for _ in range(h-1):
        costs_line = list(map(int, input().strip().split()))
        costs_line[0] += min(costs[1], costs[2])
        costs_line[1] += min(costs[0], costs[2])
        costs_line[2] += min(costs[0], costs[1])
        costs = costs_line

    print(min(costs))

# solution()


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        solution()


"""3
26 40 83
49 60 57
13 89 99"""