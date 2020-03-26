# import unittest
#
#
# class TestTopologicalSort(unittest.TestCase):
#     def setUp(self) -> None:
#         pass
#
#     def tearDown(self) -> None:
#         pass
#
#     def test_topological_sort(self):
#         pass


# def topological_sort():
from pprint import pprint

n, m = map(lambda x: int(x), input().split(' '))

degree_queue = [0] * n
graph = [[] for _ in range(n)]
result = []

for _ in range(m):
    source, target = map(lambda x: int(x) - 1, input().split(' '))
    graph[source].append(target)
    degree_queue[target] += 1

for node in range(n):
    if degree_queue[node] == 0:
        result.append(node)

for current_node in result:
    for next_node in graph[current_node]:
        degree_queue[next_node] -= 1
        if degree_queue[next_node] == 0:
            result.append(next_node)

result = list(map(lambda x: x + 1, result))
print(result)
