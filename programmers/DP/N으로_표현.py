def solution(N, number):
    result = [set() for _ in range(9)]
    for k in range(1, 9):
        result[k].add(int(str(N) * k))

    for cnt in range(1, 9):
        for i in range(1, cnt):
            for a in result[i]:
                for b in result[cnt - i]:
                    result[cnt].add(a + b)
                    result[cnt].add(a - b)
                    result[cnt].add(a * b)
                    if b != 0:
                        result[cnt].add(a // b)

            if number in result[cnt]:
                return cnt

    return -1
