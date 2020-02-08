def solution(participant, completion):
    a = dict()
    answer = ""
    for racer in participant:
        if not a.get(racer):
            a.setdefault(racer, 1)
        else:
            a[racer] += 1

    for racer in completion:
        a[racer] -= 1

    for k, v in a.items():
        if v > 0:
            answer = k

    return answer


def run_test_case():
    p = ["mislav", "stanko", "mislav", "ana"]
    c = ["stanko", "ana", "mislav"]
    print(solution(p, c))
