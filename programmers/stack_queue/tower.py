import unittest


def solution(heights):
    answer = []

    while heights:
        last = heights.pop()
        higher = -1
        for t in range(len(heights) - 1, -1, -1):
            if heights[t] > last:
                higher = t
                break
        answer = [higher + 1] + answer
    return answer


def solution_best(h):
    ans = [0] * len(h)
    for i in range(len(h) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j + 1
                break
    return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input_case1 = [6, 9, 5, 7, 4]
        self.result1 = [0, 0, 2, 2, 4]

        self.input_case2 = [3, 9, 9, 3, 5, 7, 2]
        self.result2 = [0, 0, 0, 3, 3, 3, 6]

        self.input_case3 = [1, 5, 3, 6, 7, 6, 5]
        self.result3 = [0, 0, 2, 0, 0, 5, 6]

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result1 = solution(self.input_case1)
        self.assertEqual(self.result1, result1)

        result2 = solution(self.input_case2)
        self.assertEqual(self.result2, result2)

        result3 = solution(self.input_case3)
        self.assertEqual(self.result3, result3)

    def test_solution_best(self):
        pass

    def test_solution_practice(self):
        pass
