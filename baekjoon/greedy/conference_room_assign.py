def solution(i):
    if i is None:
        con_count = int(input())
        cons = [tuple(map(int, input().split())) for _ in range(con_count)]
    else:
        i = i.split('\n')
        con_count = int(i[0])
        cons = list(map(lambda x: tuple(map(int, x.split())), i[1:]))
    cons.sort(key=lambda x: (x[1], x[0]))
    print(cons)

    count = 0
    end_time = 0
    for start, end in cons:
        if end_time <= start:
            end_time = end
            count += 1

    print(count)
    return count


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14"""
        self.result = 4

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result = solution(self.input)
        self.assertEqual(self.result, result)

    def test_solution_best(self):
        pass

    def test_solution_practice(self):
        pass