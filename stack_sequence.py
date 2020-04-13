import sys
from collections import deque


def solution():
    input = sys.stdin.readline

    n = int(input().strip())
    goal = [int(input().strip()) for _ in range(n)]
    stack = deque()
    index = 0
    result = ''
    for i in range(1, n + 1):
        stack.appendleft(i)
        result += '+\n'
        while len(stack) > 0 and index < len(goal) and stack[0] == goal[index]:
            stack.popleft()
            result += '-\n'
            index += 1
    if len(stack) != 0:
        print('NO')
    else:
        print(result.rstrip())


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        solution()
"""8
4
3
6
8
7
5
2
1"""