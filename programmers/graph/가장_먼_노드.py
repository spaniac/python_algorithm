from collections import defaultdict


def solution(n, edge):
    distance = {k + 1: 0 for k in range(n)}
    graph = defaultdict(list)

    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)

    queue = graph[1].copy()
    current_distance = 1
    while queue:
        degree_len = len(queue)
        for i in range(degree_len):
            current_node = queue.pop(0)
            if distance[current_node] == 0:
                distance[current_node] = current_distance
                queue += graph[current_node]

        current_distance += 1

    answer = list(distance.values())[1:].count(max(distance.values()))
    return answer
