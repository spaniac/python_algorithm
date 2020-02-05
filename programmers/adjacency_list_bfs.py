def solution(begin, target, words):
    if target not in words:
        return 0

    graph = get_adj_list([begin] + words)

    if not graph.get(target) or len(graph.get(target)) == 0:
        return 0

    bfs_result = bfs_for_list(graph, begin, target)
    print(bfs_result)

    answer = get_min_path_count(bfs_result)
    return answer


def can_connect(source, target):
    count = 0
    for i in range(len(source)):
        count += source[i] is target[i]

    return True if count == len(source) - 1 else False


def get_adj_list(words):
    graph = {}
    for current_node in words:
        search_nodes = set(filter(lambda x: can_connect(current_node, x), words))
        graph[current_node] = search_nodes

    return graph


# 너비 우선 탐색
def bfs_for_list(graph, begin, target):
    result = []
    queue = [(begin, [begin])]

    while queue:
        current_node, path = queue.pop(0)
        if current_node == target:
            result.append(path)
        else:
            for next_node in graph[current_node] - set(path):
                queue.append((next_node, path + [next_node]))

    return result


def get_min_path_count(result):
    return min(list(map(lambda x: len(x), result))) - 1


begin = "hit"
target = "cog"
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

print(solution(begin, target, words))
