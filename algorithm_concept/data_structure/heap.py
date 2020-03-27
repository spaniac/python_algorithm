import unittest


class MaxHeap:
    def __init__(self):
        self.max_size = 200
        self.current_size = 0
        self.heap = [0] * (self.max_size + 1)

    def insert_element(self, value):
        self.current_size += 1
        index = self.current_size

        self.heap[index] = value
        while index != 1 and self.heap[index] > self.heap[index // 2]:
            self.swap_element(index, index // 2)
            index = index // 2

    def delete_element(self):
        """
        최대힙에서 삭제는 최대값을 삭제하는 연산이므로 루트 노드를 삭제하는 것!
        """
        item = self.heap[1]
        temp = self.heap[self.current_size]
        self.current_size -= 1
        parent = 1
        child = 2

        while child <= self.current_size:
            if child < self.current_size and self.heap[child + 1] > self.heap[child]:
                child += 1
            if temp >= self.heap[child]:
                break
            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2

        self.heap[parent] = temp

        return item

    def swap_element(self, source_index, target_index):
        tmp = self.heap[source_index]
        self.heap[source_index] = self.heap[target_index]
        self.heap[target_index] = tmp


class TestCaseMaxHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.max_heap = MaxHeap()

    def tearDown(self) -> None:
        pass

    def test_insert_element(self):
        for value in range(1, 11):
            self.max_heap.insert_element(value)
            # print(self.max_heap.heap)
        expected_heap = [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
        expected_heap_size = 10
        self.assertEqual(expected_heap, self.max_heap.heap[1:11])
        self.assertEqual(expected_heap_size, self.max_heap.current_size)

    def test_delete_element(self):
        for value in range(1, 11):
            self.max_heap.insert_element(value)
        self.max_heap.delete_element()
        # print(self.max_heap.heap)
        expected_heap = [9, 8, 6, 7, 3, 2, 5, 1, 4]
        self.assertEqual(expected_heap, self.max_heap.heap[1:10])
