import sys
from collections import deque


# class Queue:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.next = None
#
#     def __init__(self):
#         self.queue_size = 0
#         self.front_node = None
#         self.back_node = None
#
#     def push(self, data):
#         new_node = self.Node(data)
#         if self.back_node is not None:
#             self.back_node.next = new_node
#         self.back_node = new_node
#         self.queue_size += 1
#         if self.front_node is None:
#             self.front_node = self.back_node
#
#     def pop(self):
#         if self.front_node is None:
#             return -1
#         pop_node = self.front_node
#         self.front_node = self.front_node.next
#         self.queue_size -= 1
#         if self.front_node is None:
#             self.back_node = None
#         return pop_node.data
#
#     def size(self):
#         return self.queue_size
#
#     def empty(self):
#         return int(self.queue_size == 0)
#
#     def front(self):
#         if self.front_node is None:
#             return -1
#         return self.front_node.data
#
#     def back(self):
#         if self.back_node is None:
#             return-1
#         return self.back_node.data


def solution():
    input = sys.stdin.readline

    queue = Queue()
    n = int(input())
    for _ in range(n):
        command = input().strip()
        if command.startswith('push'):
            command, data = command.split()
            getattr(queue, command)(int(data))
        else:
            print(getattr(queue, command)())


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, data):
        self.queue.appendleft(data)

    def pop(self):
        if bool(self.empty()):
            return -1
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def empty(self):
        return int(len(self.queue) == 0)

    def front(self):
        if bool(self.empty()):
            return -1
        return self.queue[-1]

    def back(self):
        if bool(self.empty()):
            return -1
        return self.queue[0]


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        solution()
"""15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front"""
