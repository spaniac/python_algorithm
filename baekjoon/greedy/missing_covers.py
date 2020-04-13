def solution(i):
    if i:
        input_str = i
    else:
        input_str = input()
    num_sum = 0
    input_str = input_str.split('-', 1)

    num_sum += sum(map(int, input_str[0].split('+')))
    if len(input_str) > 1:
        num_sum -= sum(map(int, input_str[1].replace('+', '-').split('-')))

    return num_sum


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input = '55-50+40'
        self.result = -35

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result = solution(self.input)
        self.assertEqual(self.result, result)
