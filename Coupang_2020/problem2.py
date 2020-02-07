"""
문제 설명
철수는 N일 동안 총 M개의 물건을 배송해야 합니다.
이때, 한꺼번에 너무 많은 물건을 배송하지 않기 위해서 연속된 T일 동안 배송한 물건 개수의 합이 K개 이하가 되도록 하려 합니다.

예를 들어, 물건 배송 기간이 4일, 배송해야 하는 물건 개수는 7개 이고, 연속된 2일 동안 배송한 물건 개수 합이 4 이하가 되도록 하는 방법은 28가지가 있습니다.
이 중 하나는 다음과 같습니다.

첫째 날   둘째 날   셋째 날   넷째 날
3   1   2   1
물건 배송 기간 N, 배송할 물건 개수 M, 연속된 날짜 길이 T, 연속된 날짜 동안 최대로 배송할 수 있는 물건 개수 K가 매개변수로 주어질 때, 조건에 맞게 물건을 배송하는 방법의 수를 return 하도록 solution 함수를 완성해주세요.

N = deliveryPeriod
M = totalItemCount
T = seriesDays
K = maxDeliverItemPerSeriesDays

제한사항
N은 1 이상 6 이하인 자연수입니다.
M은 1 이상 20 이하인 자연수입니다.
T는 1 이상 N 이하인 자연수입니다.
K는 1 이상 M 이하인 자연수입니다.
물건을 배송하지 않는 날이 있어도 괜찮습니다.
만약 물건을 배송할 수 있는 방법이 없다면 0을 return 해주세요.
입출력 예
N   M   T   K   result
2   4   1   3   3
4   7   2   4   28
4   7   2   3   0
입출력 예 설명
입출력 예 #1

물건을 배송하는 방법은 아래와 같이 5가지입니다.

첫째 날   둘째 날
0   4
1   3
2   2
3   1
4   0
이때, 첫 번째와 다섯 번째는 1일 동안 배달하는 물건 개수가 3보다 큽니다.
따라서, 연속된 1일 동안 배달하는 물건 개수가 3보다 작은 방법은 두 번째, 세 번째, 네 번째로 총 3가지입니다.

입출력 예 #2

문제의 예시와 같습니다.

입출력 예 #3

4일 동안 물건 7개를 배송하되, 연속된 2일 동안 배송한 물건 개수가 3개 이하가 되도록 하는 방법은 없으므로 0을 return 합니다.
"""
"""
dp와 조건식을 활용한 문제??
"""

def solution(N, M, T, K):
    result = delivery(N, M, T, K, [])
    return result


def delivery(N, M, T, K, queue):
    result = 0
    for item_count in range(K + 1):
        if N == 1 and M == item_count and sum(queue[1:] + [item_count]) <= K:
            result += 1
        elif len(queue) == T and sum(queue[1:] + [item_count]) <= K:
            result += delivery(N - 1, M - item_count, T, K, queue[1:] + [item_count])
        elif len(queue) < T and sum(queue + [item_count]) <= K:
            result += delivery(N - 1, M - item_count, T, K, queue + [item_count])

    return result


a = solution(4, 7, 2, 4)
print(a)
