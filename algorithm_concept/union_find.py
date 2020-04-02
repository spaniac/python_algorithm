class UnionFind:
    def __init__(self, num_of_nodes):
        self.root = [n for n in range(num_of_nodes)]

    def find(self, node):
        return self.find(self.root[node]) if self.root[node] != node else node

    def union(self, node1, node2):
        root_of_node1 = self.find(node1)
        root_of_node2 = self.find(node2)
        self.root[root_of_node2] = root_of_node1

    def find_with_compress(self, node):
        while self.root[node] != node:
            self.root[node] = self.find_with_compress(self.root[node])
            node = self.root[node]
        return node

    def union_with_compress(self, node1, node2):
        root_of_node1 = self.find_with_compress(node1)
        root_of_node2 = self.find_with_compress(node2)
        self.root[root_of_node2] = root_of_node1

    def is_cycled(self, node1, node2):
        return self.find(node1) == self.find(node2)


import unittest


class TestUnionFind(unittest.TestCase):
    def setUp(self) -> None:
        self.union_find = UnionFind(8)

    def tearDown(self) -> None:
        super(TestUnionFind, self).tearDown()

    def test_union_find1(self):
        self.union_find.union(0, 5)
        self.union_find.union(5, 7)
        self.union_find.union(1, 2)
        self.union_find.union(4, 2)
        self.union_find.union(3, 5)
        self.union_find.union(6, 5)
        print(self.union_find.root)

    def test_union_find2(self):
        self.union_find.union_with_compress(0, 5)
        self.union_find.union_with_compress(5, 7)
        self.union_find.union_with_compress(1, 2)
        self.union_find.union_with_compress(4, 2)
        self.union_find.union_with_compress(3, 5)
        self.union_find.union_with_compress(6, 5)

        self.union_find.find_with_compress(2)
        # self.union_find.find_with_compress(5)
        print(self.union_find.root)
