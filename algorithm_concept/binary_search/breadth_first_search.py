import unittest


class BFS:
    def __init__(self):
        self.graph = None
        self.visited = []
        self.queue = []

    def add_undirected_edge(self, node1, node2):
        if self.graph is None:
            raise Exception("There's no graph")
        self.graph[node1].append(node2)

    def make_graph(self, num_of_node, edge_list, start):
        graph = [[] for _ in range(num_of_node)]
        for node1, node2 in edge_list:
            graph[node1].append(node2)
            graph[node2].append(node1)

        for i in graph:
            i.sort()

        self.graph = graph
        self.visited = []
        self.queue = [start]

    def search(self):
        if self.graph is None:
            raise Exception("There's no graph")
        while self.queue:
            current_node = self.queue.pop(0)
            if current_node in self.visited:
                continue
            self.visited.append(current_node)
            for next_node in self.graph[current_node]:
                self.queue.append(next_node)

        return self.visited


class TestBFS(unittest.TestCase):
    def setUp(self) -> None:
        self.bfs = BFS()
        self.edge_list = [(0, 1), (1, 2), (0, 2), (2, 3), (3, 4), (2, 4), (4, 0)]
        self.expected = [0, 1, 2, 4, 3]

    def tearDown(self) -> None:
        pass

    def test_bfs(self):
        self.bfs.make_graph(5, self.edge_list, 0)
        result = self.bfs.search()
        self.assertEqual(self.expected, result)
