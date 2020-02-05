def solution(begin, target, words):
    if target not in words:
        return 0

    graph = get_adj_list([begin] + words)
    if not graph.get(target):
        return 0

    dfs_result = dfs_for_list(graph, begin, target)
    print(dfs_result)

    answer = get_min_path_count(dfs_result)
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


# 깊이 우선 탐색
def dfs_for_list(graph, begin, target):
    result = []
    stack = [(begin, [begin])]

    while stack:
        current_node, path = stack.pop()
        if current_node == target:
            result.append(path)
        else:
            for next_node in graph[current_node] - set(path):
                stack.append((next_node, path + [next_node]))

    return result


def get_min_path_count(result):
    return min(set(map(lambda x: len(x), result))) - 1


begin = "hit"
target = "cog"
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

print(solution(begin, target, words))
