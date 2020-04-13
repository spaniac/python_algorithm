import sys
from collections import deque


def solution():
    input = sys.stdin.readline

    n = int(input().strip())
    for _ in range(n):
        stack = deque()
        ps = input().strip()
        is_vps = True
        for i in ps:
            if i == '(':
                stack.appendleft(i)
            else:
                if len(stack) > 0:
                    stack.popleft()
                else:
                    is_vps = False
                    break
        print('YES' if is_vps and len(stack) == 0 else 'NO')


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        pass
