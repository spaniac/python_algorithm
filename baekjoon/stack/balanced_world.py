import sys
from collections import deque


def solution():
    input = sys.stdin.readline

    while True:
        ps = input().rstrip()
        if ps[0] == '.':
            break

        stack = deque()
        is_vps = True
        for i in ps:
            if i in ['(', '[']:
                stack.appendleft(i)
            elif i in [')', ']']:
                if len(stack) > 0:
                    if (i == ')' and stack[0] == '(') or (i == ']' and stack[0] == '['):
                        stack.popleft()
                    else:
                        is_vps = False
                        break
                else:
                    is_vps = False
                    break
        print('yes' if is_vps and len(stack) == 0 else 'no')


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        solution()
