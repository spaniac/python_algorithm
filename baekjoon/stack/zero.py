import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    n = int(input().strip())
    stack = deque()
    for _ in range(n):
        num = int(input().strip())
        if num == 0:
            stack.popleft()
        else:
            stack.appendleft(num)

    print(sum(stack))


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        pass
