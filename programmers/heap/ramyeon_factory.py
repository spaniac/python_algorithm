from heapq import *


def solution(stock, dates, supplies, k):
    answer = 0
    pq = []
    index = 0
    while stock < k:
        for a in range(index, len(dates)):
            if dates[a] <= stock:
                heappush(pq, (-supplies[a], supplies[a]))
                index += 1
            else:
                break
        stock += heappop(pq)[1]
        answer += 1

    return answer


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input1 = (4, [4, 10, 15], [20, 5, 10], 30)
        self.result1 = 2

        self.input2 = (4, [1, 3, 8, 16, 24], [5, 1, 7, 14, 6], 30)
        self.result2 = 3

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result = solution(*self.input1)
        self.assertEqual(self.result1, result)

        result2 = solution(*self.input2)
        self.assertEqual(self.result2, result2)

    def test_solution_best(self):
        pass

    def test_solution_practice(self):
        pass
