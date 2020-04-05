from heapq import heapify


# class MinHeap:
#     def __init__(self):
#         self.heap = [0] * 1000001
#         self.size = 0
#         self.root = 1
#
#     def insert(self, data):
#         self.size += 1
#         self.heap[self.size] = data
#         current = self.size
#         parent = current // 2
#         while parent >= self.root and self.heap[parent] > data:
#             temp = self.heap[current]
#             self.heap[current] = self.heap[parent]
#             self.heap[parent] = temp
#             current = parent
#             parent //= 2
#         self.heap[current] = data
#
#     def delete(self):
#         pop_data = self.heap[self.root]
#         last_data = self.heap[self.size]
#         self.size -= 1
#
#         current = self.root
#         child = self.root * 2
#         while child <= self.size:
#             if child < self.size and self.heap[child] > self.heap[child + 1]:
#                 child += 1
#             if self.heap[child] > last_data:
#                 break
#             self.heap[current] = self.heap[child]
#             current = child
#             child *= 2
#
#         self.heap[current] = last_data
#
#         return pop_data
#
#     def get_min(self):
#         return min(self.heap[self.root:self.root + self.size])
#
#
# def solution(scoville, K):
#     answer = 0
#     min_heap = MinHeap()
#     for s in scoville:
#         min_heap.insert(s)
#     while min_heap.get_min() < K:
#         first_min = min_heap.delete()
#         second_min = min_heap.delete()
#         new_food = first_min + second_min * 2
#         min_heap.insert(new_food)
#         answer += 1
#     return answer
from heapq import *


def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heappush(heap, s)

    while heap[0] < K:
        if len(heap) < 2:
            return -1
        first = heappop(heap)
        second = heappop(heap)
        heappush(heap, first + second * 2)
        answer += 1

    return answer

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input = ([1, 2, 3, 9, 10, 12], 7)
        self.result = 2

        self.input2 = ([1, 2, 3, 9, 10, 12], 7)
        self.result2 = 2

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result = solution(*self.input)
        self.assertEqual(self.result, result)

    def test_solution_best(self):
        pass

    def test_solution_practice(self):
        pass
