def solution(progresses, speeds):
    answer = []

    day = 1
    while progresses and speeds:
        count = 0
        while progresses and speeds and progresses[0] + speeds[0] * day >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if count > 0:
            answer.append(count)
        day += 1

    return answer


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input1 = ([93, 30, 55], [1, 30, 5, ])
        self.result1 = [2, 1]

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result = solution(*self.input1)
        self.assertEqual(self.result1, result)

    def test_solution_best(self):
        pass

    def test_solution_practice(self):
        pass
