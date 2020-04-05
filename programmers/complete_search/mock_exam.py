def solution(answers):
    part = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result = [0, 0, 0]
    for i in range(len(part)):
        for j in range(len(answers)):
            result[i] += part[i][j % len(part[i])] == answers[j]

    answer = []
    max_result = max(result)
    for i in range(len(result)):
        if result[i] == max_result:
            answer.append(i + 1)

    return answer


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input1 = [1, 2, 3, 4, 5]
        self.result1 = [1]
        self.input2 = [1, 3, 2, 4, 2]
        self.result2 = [1, 2, 3]

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result1 = solution(self.input1)
        self.assertEqual(self.result1, result1)
        result2 = solution(self.input2)
        self.assertEqual(self.result2, result2)

    def test_solution_best(self):
        pass

    def test_solution_practice(self):
        pass
