import sys
from collections import deque


# class Stack:
#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.next = None
#
#     def __init__(self):
#         self.top_node = None
#         self.stack_size = 0
#
#     def push(self, data):
#         new_node = self.Node(data)
#         if not self.empty():
#             new_node.next = self.top_node
#         self.top_node = new_node
#         self.stack_size += 1
#
#     def pop(self):
#         if not self.empty():
#             pop_node = self.top_node
#             self.top_node = self.top_node.next
#             self.stack_size -= 1
#             return pop_node.data
#         else:
#             return -1
#
#     def size(self):
#         return self.stack_size
#
#     def empty(self):
#         return int(self.stack_size == 0)
#
#     def top(self):
#         return self.top_node.data if not self.empty() else -1


class StackDeq:
    def __init__(self):
        self.deque = deque()

    def push(self, data):
        self.deque.appendleft(data)

    def pop(self):
        if self.empty():
            return -1
        return self.deque.popleft()

    def size(self):
        return len(self.deque)

    def empty(self):
        return int(len(self.deque) == 0)

    def top(self):
        if self.empty():
            return -1
        return self.deque[0]


def solution(i):
    # n = int(input())
    n = int(i[0])
    stack = StackDeq()
    for j in range(1, n + 1):
        command = i[j]
        if command.startswith('push'):
            command, data = command.split()
            getattr(stack, command)(int(data))
        else:
            print(getattr(stack, command)())


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input = """14
push 1
push 2
top
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
top"""
        self.input = self.input.split('\n')

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        stack = StackDeq()
        input = sys.stdin.readline
        n = int(input().strip())
        for _ in range(n):
            command = input().strip()
            if command.startswith('push'):
                command, data = command.split()
                getattr(stack, command)(int(data))
            else:
                print(getattr(stack, command)())
