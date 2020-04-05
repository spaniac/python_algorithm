import collections
import unittest


def solution(bridge_length, weight, truck_weights):
    answer = 1
    trucks = collections.deque([0, truck] for truck in truck_weights)
    bridge = collections.deque([trucks.popleft()])
    while bridge:
        for truck in bridge:
            truck[0] += 1
        if bridge[0][0] == bridge_length:
            bridge.popleft()
        if trucks and trucks[0][1] <= weight - sum(map(lambda x: x[1], bridge)):
            bridge.append(trucks.popleft())
        answer += 1
    return answer


DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution_best(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input1 = (2, 10, [7, 4, 5, 6])
        self.result1 = 8

        self.input2 = (100, 100, [10])
        self.result2 = 101

        self.input3 = (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        self.result3 = 110

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result1 = solution(*self.input1)
        self.assertEqual(self.result1, result1)

        result2 = solution(*self.input2)
        self.assertEqual(self.result2, result2)

        result3 = solution(*self.input3)
        self.assertEqual(self.result3, result3)

    def test_solution_best(self):
        result1 = solution_best(*self.input1)
        self.assertEqual(self.result1, result1)

        result2 = solution_best(*self.input2)
        self.assertEqual(self.result2, result2)

        result3 = solution_best(*self.input3)
        self.assertEqual(self.result3, result3)

    def test_solution_practice(self):
        pass
