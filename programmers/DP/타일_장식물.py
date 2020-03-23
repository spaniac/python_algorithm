def solution(N):
    answer_list = [0, 4, 6]
    if N <= 2:
        return answer_list[N]

    for a in range(3, N + 1):
        answer_list.append(answer_list[a - 2] + answer_list[a - 1])
    return answer_list[-1]
