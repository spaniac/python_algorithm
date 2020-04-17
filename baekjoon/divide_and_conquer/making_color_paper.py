import sys

result = [0, 0]


def solution():
    input = sys.stdin.readline
    n = int(input())
    paper = []
    for _ in range(n):
        l = list(map(int, input().strip().split()))
        paper.append(l)
    recursive(paper, n)
    global result
    print("{} {}".format(*result))


def recursive(paper, num):
    global result
    total_sum = sum(map(sum, paper))
    if total_sum == num * num:
        result[1] += 1
    elif total_sum == 0:
        result[0] += 1
    else:
        itv = num // 2
        for i in range(2):
            for j in range(2):
                quarter = []
                for k in range(itv):
                    quarter.append(paper[i * itv: (i + 1) * itv][k][j * itv:(j + 1) * itv])
                recursive(quarter, itv)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        solution()


"""
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
"""