def solution():
    num_of_coin, goal = map(int, input().split(' '))
    coins = [int(input()) for _ in range(num_of_coin)]

    count = 0
    for i in range(1, num_of_coin + 1):
        div, mod = divmod(goal, coins[-i])
        count += div
        goal = mod

    print(count)
    return count


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input1 = """10 4200
1
5
10
50
100
500
1000
5000
10000
50000"""
        self.result1 = 6

        self.input2 = """10 4790
1
5
10
50
100
500
1000
5000
10000
50000"""
        self.result2 = 12

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result = solution()
        self.assertEqual(self.result1, result)
        result = solution()
        self.assertEqual(self.result2, result)

    def test_solution_best(self):
        pass

    def test_solution_practice(self):
        pass
