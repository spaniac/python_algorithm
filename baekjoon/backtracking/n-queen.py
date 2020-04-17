import sys

"""
이 문제를 파이썬으로 통과하기 위해서는 능숙한 최적화가 필요하다
    -> 일반적인 코드로는 통과히기 어렵다.
"""


def dfs(arr):
    global result
    if len(arr) == n:
        result += 1
        return

    next_pos = set(range(n)).difference(arr)
    dist = range(len(arr), 0, -1)
    next_pos.difference_update(map(lambda x, y: y - x, dist, arr))
    next_pos.difference_update(map(lambda x, y: y + x, dist, arr))

    # next_pos = list(set(range(num)).difference(arr))
    # for i in range(len(arr)):
    #     dist = len(arr) - i
    #     if arr[i] + dist in next_pos:
    #         next_pos.remove(arr[i] + dist)
    #     if arr[i] - dist in next_pos:
    #         next_pos.remove(arr[i] - dist)

    for pos in next_pos:
        dfs(arr + [pos])


n = None
result = 0


def solution():
    input = sys.stdin.readline
    global n
    n = int(input())
    # n = 8
    for i in range(n):
        dfs([i])
    print(result)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        solution()
