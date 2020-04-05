def solution(budgets, M):
    budgets.sort()
    answer = sum(budgets) // len(budgets)
    index = len(budgets)//2
    while True:
        while index > 0 and budgets[index - 1] > answer:
            index -= 1
        while index < len(budgets) - 1 and budgets[index + 1] < answer:
            index += 1
        b = sum(budgets[:index]) + answer * (len(budgets) - index)
        if b <= M:
            return answer
        else:
            answer -= 1

    # return answer + 1