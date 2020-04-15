import sys


def solution(num):
    if num < 3:
        return num
    array = [0] * (num + 1)
    for i in range(3):
        array[i] = i
    for i in range(3, num + 1):
        array[i] = (array[i - 1] + array[i - 2]) % 15746
    return array[num]


a = sys.stdin.readline
print(solution(int(a())))

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        a = sys.stdin.readline
        print(solution(int(a())) % 15746)
