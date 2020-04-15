import sys


def solution(num):
    if num < 4:
        return 1
    if num < 6:
        return 2
    array = [0] * (num + 1)
    array[1] = array[2] = array[3] = 1
    array[4] = array[5] = 2
    for i in range(6, num + 1):
        array[i] = array[i - 5] + array[i - 1]
    return array[num]


input = sys.stdin.readline
for _ in range(int(input())):
    print(solution(int(input())))

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        input = sys.stdin.readline
        for _ in range(int(input())):
            print(solution(int(input())))
