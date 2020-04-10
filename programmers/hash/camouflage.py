def solution(clothes):
    from collections import Counter
    from functools import reduce
    counter = Counter([c_type for _, c_type in clothes])
    answer = reduce(lambda x, y: x * (y + 1), counter.values(), 1) - 1
    return answer

# def solution(clothes):
#     answer = 1
#     clothes_dict = {}
#     for v, k in clothes:
#         if not clothes_dict.get(k):
#             clothes_dict.setdefault(k, [v])
#         else:
#             clothes_dict[k] += [v]
#
#     for k, v in clothes_dict.items():
#         answer *= len(v) + 1
#     return answer - 1
