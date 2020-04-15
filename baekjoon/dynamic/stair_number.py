import sys


def solution():
    input = sys.stdin.readline
    n = int(input())
    if n == 1:
        return 9
    array = [[0] * 10 for _ in range(n + 1)]
    array[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                array[i][j] = array[i - 1][j + 1]
            elif 0 < j < 9:
                array[i][j] = array[i - 1][j - 1] + array[i - 1][j + 1]
            else:
                array[i][j] = array[i - 1][j - 1]
    return sum(array[n]) % 1000000000


# print(solution())

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        print(solution())
