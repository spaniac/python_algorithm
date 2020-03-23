def solution(triangle):
    for depth in range(1, len(triangle)):
        for width in range(len(triangle[depth])):
            if width == 0:
                triangle[depth][width] += triangle[depth - 1][width]
            elif 0 < width < len(triangle[depth]) - 1:
                triangle[depth][width] += max(triangle[depth - 1][width - 1], triangle[depth - 1][width])
            else:
                triangle[depth][width] += triangle[depth - 1][width - 1]

    answer = max(triangle[len(triangle) - 1])
    return answer

# def solution(triangle):
#     result = 0
#     queue = [(triangle[0][0], (0, 0))]
#
#     while queue:
#         sums, position = queue.pop()
#         depth, width = position
#         if depth == len(triangle) - 1:
#             result = max(result, sums)
#         else:
#             queue += [(sums + triangle[depth + 1][width], (depth + 1, width))]
#             queue += [(sums + triangle[depth + 1][width + 1], (depth + 1, width + 1))]
#
#     return answer
#     answer = result


# 미친놈의 솔루션
# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
