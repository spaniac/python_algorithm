import unittest


class MyStack:
    class StackNode:
        def __init__(self, data):
            self.next_node = None
            self.data = data

    def __init__(self):
        self.top_node = None
        self.size = 0

    def push(self, data):
        new_node = self.StackNode(data)
        new_node.next_node = self.top_node
        self.top_node = new_node
        self.size += 1

    def pop(self):
        if self.top_node is None or self.size == 0:
            raise Exception("such no nodes")
        pop_node = self.top_node
        self.top_node = self.top_node.next_node
        self.size -= 1
        return pop_node.data

    def peek(self):
        if self.top_node is None or self.size == 0:
            raise Exception("such no nodes")
        return self.top_node.data

    def is_empty(self):
        if self.top_node is None or self.size == 0:
            return True
        return False

    def print_all(self):
        current_node = self.top_node
        line = ''
        while current_node is not None:
            line += str(current_node.data) + ' '
            current_node = current_node.next_node
        print(line)


class TestMyStackTest(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = MyStack()

    def tearDown(self) -> None:
        pass

    def test_push(self):
        for a in range(100):
            self.stack.push(a)
        self.stack.print_all()

    def test_pop(self):
        with self.assertRaises(Exception):
            self.stack.pop()
        self.stack.push(100)
        self.stack.push('push push')
        pop_data = self.stack.pop()
        self.assertEqual('push push', pop_data)
        self.stack.pop()
        with self.assertRaises(Exception):
            self.stack.pop()

    def test_peek(self):
        with self.assertRaises(Exception):
            self.stack.peek()
        self.stack.push('push more!')
        self.stack.push(13)
        self.assertEqual(13, self.stack.peek())
        self.stack.pop()
        self.assertEqual('push more!', self.stack.peek())
        self.stack.pop()
        with self.assertRaises(Exception):
            self.stack.peek()

    def test_print_all(self):
        for a in range(10):
            self.stack.push('push{}'.format(a))
        self.stack.print_all()
