import sys

# def solution():
#     input = sys.stdin.readline
#     n = 1
#     result = 0
#     start = 0
#     while start < n:
#         queue = deque([start])
#
#         if len(queue) == n:
#             result += 1
#         else:
#             for nc in range(n):
#                 queue.append(nc)
#                 if is_possible(pos, nc):
#                     queue.append(pos + [nc])
#         start += 1
#     print(result)
#
#
# def is_possible(pos, nc):
#     if nc in pos:
#         return False
#     nr = len(pos)
#     for r, c in enumerate(pos):
#         if abs(nr - r) == abs(nc - c):
#             return False
#     return True


result = 0
n = None
col = [-1] * 15
c = None

def solution2():
    input = sys.stdin.readline
    # n = int(input())
    global n
    n = 12
    global col
    global result
    global c
    c = range(n)
    for i in c:
        col[0] = i
        dfs(0)
    print(result)


def dfs(row):
    global n
    global result
    global col
    global c
    if row == n - 1:
        result += 1
    else:
        for i in c:
            col[row + 1] = i
            if is_possible2(row + 1):
                dfs(row + 1)
            else:
                col[row + 1] = -1
    col[row] = -1


def is_possible2(row):
    global col
    if col[row] in col[:row]:
        return False
    for i in range(row):
        if abs(row - i) == abs(col[row] - col[i]):
            return False
    return True


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        # solution()
        solution2()
