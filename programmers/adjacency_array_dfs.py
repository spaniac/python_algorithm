def solution(begin, target, words):
    if target not in words:
        return 0

    all_words = [begin] + words
    graph = get_relation_graph(all_words)

    bfs_result = bfs_for_arr(graph, all_words.index(begin), all_words.index(target))
    print(bfs_result)
    answer = get_min_path_count(bfs_result)
    return answer


def get_relation_graph(words):
    graph = [[0] * len(words) for _ in range(len(words))]
    for i in range(len(words)):
        column = list(map(lambda x: can_connect(words[i], x), words))
        graph[i] = column

    return graph


def can_connect(source, target):
    count = 0
    for i in range(len(source)):
        count += source[i] is target[i]

    return True if count == len(source) - 1 else False


def bfs_for_arr(graph, start, target):
    result = []
    queue = [(start, [start])]

    while queue:
        current_node, current_path = queue.pop()
        if current_node == target:
            result.append(current_path)
        else:
            if graph[current_node].count(True) > 0:
                for next_node in range(len(graph)):
                    if graph[current_node][next_node] is True:
                        graph[next_node][current_node] = False
                        queue.append((next_node, current_path + [next_node]))

    return result


def get_min_path_count(result):
    return min(list(map(lambda x: len(x), result))) - 1


begin = "hit"
target = "cog"
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

print(solution(begin, target, words))
