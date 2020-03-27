import unittest


class MyQueue:
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next_node = None

    def __init__(self):
        self.first_node = None
        self.last_node = None

    def add(self, data):
        new_node = self.QueueNode(data)

        if self.last_node is not None:
            self.last_node.next_node = new_node
        self.last_node = new_node
        if self.first_node is None:
            self.first_node = self.last_node

    def remove(self):
        if self.first_node is None:
            raise Exception("such no nodes")
        data = self.first_node.data
        self.first_node = self.first_node.next_node
        if self.first_node is None:
            self.last_node.next = None
        return data

    def peek(self):
        if self.first_node is None:
            raise Exception("such no nodes")
        return self.first_node.data

    def is_empty(self):
        return True if self.first_node is None else False

    def print_all(self):
        if self.first_node is None:
            print("such no nodes")
        line = ""
        current_node = self.first_node
        while current_node is not None:
            line += str(current_node.data) + " "
            current_node = current_node.next_node
        print(line)


class TestMyQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = MyQueue()

    def tearDown(self) -> None:
        pass

    def test_add_node(self):
        for a in range(100):
            self.queue.add(a)
        print(self.queue.print_all())

    def test_remove_node(self):
        with self.assertRaises(Exception):
            self.queue.remove()
        self.queue.add(['ase', 'fes'])
        self.assertEqual(['ase', 'fes'], self.queue.remove())
        with self.assertRaises(Exception):
            self.queue.remove()

    def test_peek_data(self):
        with self.assertRaises(Exception):
            self.queue.peek()
        self.queue.add(3)
        self.assertEqual(3, self.queue.peek())
        self.queue.add(['hello', 'world'])
        self.assertEqual(3, self.queue.peek())
        self.queue.remove()
        self.assertEqual(['hello', 'world'], self.queue.peek())
        self.queue.remove()
        with self.assertRaises(Exception):
            self.queue.remove()
        with self.assertRaises(Exception):
            self.queue.peek()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.add(3)
        self.queue.add(['hello', 'world'])
        self.assertFalse(self.queue.is_empty())

    def test_print_all(self):
        self.queue.print_all()
        self.queue.add(1)
        self.queue.add(3)
        self.queue.add(['ase', 'fes'])
        self.queue.print_all()
