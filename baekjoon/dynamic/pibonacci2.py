import sys


def solution(num):
    if num == 0:
        return 1, 0
    if num == 1:
        return 0, 1
    array = [tuple() for _ in range(num + 1)]
    array[0] = (1, 0)
    array[1] = (0, 1)
    for i in range(2, num + 1):
        array[i] = (array[i - 1][0] + array[i - 2][0], array[i - 1][1] + array[i - 2][1])
    return array[num]


stdin = sys.stdin.readline
t = int(stdin())
for _ in range(t):
    result = solution(int(stdin()))
    print('{} {}'.format(result[0], result[1]))

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        stdin = sys.stdin.readline
        t = int(stdin())
        for _ in range(t):
            result = solution(int(stdin()))
            print('{} {}'.format(result[0], result[1]))
