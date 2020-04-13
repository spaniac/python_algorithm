num = int(input())
line_list = sorted(list(map(int, input().split())))

answer = 0
for i in range(len(line_list) + 1):
    answer += sum(line_list[:i])

print(answer)



import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        pass

    def test_solution_best(self):
        pass

    def test_solution_practice(self):
        pass