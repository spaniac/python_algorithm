from collections import deque


class Queue:
    def __init__(self, priorities):
        self._queue = deque(priorities)

    def pop(self):
        return self._queue.popleft()

    def push(self, data):
        self._queue.append(data)

    def get_highest_priority(self):
        return max(self._queue) if self._queue else 0

    def get_order(self, location):
        count = 1

        while self._queue:
            p = self._queue.popleft()
            if p >= self.get_highest_priority():
                if location == 0:
                    return count
                else:
                    count += 1
                    location -= 1
            else:
                self._queue.append(p)
                if location == 0:
                    location = len(self._queue) - 1
                else:
                    location -= 1

    def __len__(self):
        return len(self._queue)


def solution(priorities, location):
    a = Queue(priorities)
    answer = a.get_order(location)
    return answer


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input1 = [2, 1, 3, 2]
        self.queue1 = Queue(self.input1)
        self.result1 = 1

        self.input2 = [1, 1, 9, 1, 1, 1]
        self.queue2 = Queue(self.input2)
        self.result2 = 5

        self.input3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.queue3 = Queue(self.input3)
        # self.result3 =

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result1 = self.queue1.get_order(2)
        self.assertEqual(self.result1, result1)
        result2 = self.queue2.get_order(0)
        self.assertEqual(self.result2, result2)

    def test_solution_best(self):
        result3 = self.queue3.get_order(9)
        print(result3)
        pass

    def test_solution_practice(self):
        pass
