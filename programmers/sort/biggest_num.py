def solution(numbers):
    num_str = sorted([str(num) for num in numbers], key=lambda x: x*3, reverse=True)
    return str(int(''.join(num_str)))


import unittest
from random import *


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input1 = [6, 10, 2]
        self.result1 = "6210"
        self.input2 = [3, 30, 34, 5, 9]
        self.result2 = "9534330"
        self.input3 = [randint(0, 1001) for _ in range(5)]

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
