"""
집 여러 채가 일정한 간격으로 늘어선 마을이 있습니다.
지훈이가 물건을 배송한 집들의 위치가 주어지면, 지훈이가 물건을 배송하지 않은 집들의 위치를 구하려 합니다.
집의 위치는 수직선 위 좌표로 표시하며, 각 좌표에는 집이 한 채씩 있습니다.

다음은 집 5채가 일정한 간격으로 늘어서 있으며, 좌표값이 가장 작은 집의 위치가 -5, 가장 큰 집의 위치가 3인 마을의 예시입니다.

position_1.png

집 5채가 일정한 간격으로 늘어서 있으므로, 각 집의 위치는 위 그림과 같습니다.
이때, 지훈이가 물건을 배송한 집의 위치가 [-1, -3, 3]이라면, 지훈이가 물건을 배송하지 않은 집의 위치는 [-5, 1]입니다.

집의 수 n, 좌표값이 가장 작은 집의 위치 min_position, 좌표값이 가장 큰 집의 위치 max_position,
지훈이가 물건을 배송한 집의 위치가 담긴 배열 positions가 매개변수로 주어질 때,
지훈이가 물건을 배송하지 않은 집의 위치를 오름차순 정렬해서 return 하도록 solution 함수를 완성해주세요.

n = totalTargetHouse
min_position
max_position
positions

제한사항
n은 3 이상 100,000 이하인 자연수입니다.
min_position, max_position은 -1,000,000,000 이상 1,000,000,000 이하인 정수입니다.
min_position은 항상 max_position 보다 작습니다.
positions의 길이는 1 이상 n - 1 이하입니다.
모든 집의 좌표가 정수인 경우만 입력으로 주어집니다.
입출력 예
n   min_position   max_position   positions   result
5   -5   3   [-1, -3, 3]   [-5, 1]
6   -10   10   [6, -10, 2, -6]   [-2, 10]
입출력 예 설명
입출력 예 #1

문제의 예시와 같습니다.

입출력 예 #2

집 6채가 일정한 간격으로 늘어서 있으므로, 각 집의 위치는 [-10, -6, -2, 2, 6, 10]입니다.
지훈이가 물건을 배송한 집의 위치가 [6, -10, 2, -6]이므로, 물건을 배송하지 않은 집의 위치는 [-2, 10]입니다.
"""


def solution(n, min_position, max_position, positions):
    interval = get_interval(n, min_position, max_position)
    all_positions = get_all_positions(min_position, n, interval)
    answer = get_undelivered_position(all_positions, positions)
    return answer


def get_interval(n, min_position, max_position):
    return int((max_position - min_position) / (n - 1))


def get_all_positions(start_position, position_count, interval):
    return [start_position + i * interval for i in range(position_count)]


def get_undelivered_position(all_position, delivered_position):
    return sorted(list(set(all_position) - set(delivered_position)))
