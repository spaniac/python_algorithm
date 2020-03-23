def solution(participant, completion):
    from collections import Counter
    counter_result = Counter(participant) - Counter(completion)
    return list(counter_result.keys())[0]

# def solution(participant, completion):
#     a = dict()
#     answer = ""
#     for racer in participant:
#         if not a.get(racer):
#             a.setdefault(racer, 1)
#         else:
#             a[racer] += 1

#     for racer in completion:
#         a[racer] -= 1

#     for k, v in a.items():
#         if v > 0:
#             answer = k

#     return answer
