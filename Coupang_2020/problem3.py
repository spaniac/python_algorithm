"""
로드 밸런싱(Load Balancing)이란 여러 대의 서버에 사용자 요청을 분산하는 네트워크 기술입니다.
대표적인 로드 밸런싱 알고리즘은 다음과 같습니다.

Round Robin(순차방식): 사용자 요청을 서버에 순차적으로 하나씩 분배합니다.
Least Connection(최소 접속 방식): 열려있는 커넥션이 가장 적은 서버로 사용자 요청을 분배합니다.
두 알고리즘 각각 장단점이 있기 때문에 서버 성능, 요청 및 트래픽 등을 고려하여 적절한 알고리즘을 선택해야 합니다.

본 문제에서는 각 요청이 들어온 시각과 처리시간이 로그 문자열 형태로 주어질 때, 모든 요청을 처리하는데 두 알고리즘 중 어떤 것이 얼마만큼 더 빠른지 구해야 합니다.
각 서버는 한 번에 하나의 요청만 처리할 수 있다고 가정하며, 각 요청은 서버에 할당된 순서대로 처리합니다.

서버는 numServer대만큼 있으며, 각 서버에는 1번부터 numServer까지 번호가 하나씩 붙어있습니다.

Round Robin은 1번 서버부터 마지막 서버까지 번호가 증가하는 순서대로 하나씩 요청을 할당한 후 다시 1번 서버부터 요청을 할당합니다.

Least Connection은 열려있는 커넥션 수(각 서버에 현재 할당된 요청의 개수)가 가장 적은 서버로 요청을 할당합니다.
커넥션 수가 가장 적은 서버가 여러 대라면 그중 번호가 가장 작은 서버로 할당합니다.
이때, 서버에 할당된 요청이 완료되는 시각과 새로운 요청이 들어온 시각이 같은 경우, 서버에 할당된 요청이 먼저 완료된다고 가정합니다.

성능이 동일한 전체 서버 수 numServer와 로그 문자열이 담긴 배열 logs가 매개변수로 주어질 때, 어떤 알고리즘이 얼마만큼 더 빠른지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해주세요.

제한사항
numServer는 1 이상 10 이하인 자연수입니다.
logs의 길이는 1 이상 10,000 이하입니다.
logs의 원소는 "요청시각 처리시간"형식의 문자열입니다.
요청시각과 처리시간은 공백으로 구분되어 주어집니다.
요청시각은 HH:MM:SS.SSS 형식의 문자열로, 24시간 표기법을 사용합니다.
처리시간은 S.SSS 형식의 문자열입니다.
예를 들어 13:22:08.030 0.100은 13시 22분 8.03초에 요청이 들어왔으며, 요청을 처리하려면 0.1초가 필요하다는 뜻입니다.
처리시간은 최대 3초입니다.
요청시각은 00:00:00.000 ~ 23:59:59.999로 주어지며, 하루 동안의 로그를 나타냅니다.
요청시각이 중복되는 경우는 없습니다.
logs의 원소는 요청시각 순으로 정렬되어 있습니다.
배열에 [더 빠른 알고리즘 번호, 시간 차이]를 순서대로 담아 반환해주세요.
Round Robin 알고리즘의 번호는 1, Least Connection 알고리즘의 번호는 2입니다.
시간 차이는 ms(밀리세컨드) 단위로 나타냅니다.
예를 들어 Least Connection이 13.501초만큼 더 빠르다면 [2, 13501]을 반환합니다.
두 알고리즘에 차이가 없다면 [0, 0]을 반환합니다.
입출력 예
numServer   logs   result
2   ["12:00:00.100 0.400","12:00:00.200 0.500","12:00:00.300 0.100","12:00:00.400 0.600","12:00:00.500 0.200","12:00:00.600 0.400"]   [2, 400]
입출력 예
입출력 예 #1

입력으로 주어진 로그는 다음과 같습니다.

번호   요청 시각   처리 시간(초)
1   12:00:00.100   0.400
2   12:00:00.200   0.500
3   12:00:00.300   0.100
4   12:00:00.400   0.600
5   12:00:00.500   0.200
6   12:00:00.600   0.400
Round Robin의 경우 각 요청이 다음과 같이 분배됩니다:

시각   서버 1이 처리 중인 요청   서버 1에 대기 중인 요청   서버 2가 처리 중인 요청   서버 2에 대기 중인 요청
12:00:00.100   1번   [없음]   없음   [없음]
12:00:00.200   1번   [없음]   2번   [없음]
12:00:00.300   1번   [3번]   2번   [없음]
12:00:00.400   1번   [3번]   2번   [4번]
12:00:00.500   3번   [5번]   2번   [4번]
12:00:00.600   5번   [없음]   2번   [4번, 6번]
12:00:00.700   5번   [없음]   4번   [6번]
12:00:00.800   없음   [없음]   4번   [6번]
...
12:00:01.300   없음   [없음]   6번   [없음]
...
12:00:01.700   없음   [없음]   없음   [없음]
1번 서버는 12:00:00.800에 할당된 요청을 모두 처리하며, 2번 서버는 12:00:01.700에 할당된 요청을 모두 처리합니다.
따라서 모든 요청을 처리한 시각은 12:00:01.700입니다.

Least Connection의 경우 각 요청이 다음과 같이 분배됩니다:

시각   서버 1이 처리 중인 요청   서버 1에 대기 중인 요청   서버 2가 처리 중인 요청   서버 2에 대기 중인 요청
12:00:00.100   1번   [없음]   없음   [없음]
12:00:00.200   1번   [없음]   2번   [없음]
12:00:00.300   1번   [3번]   2번   [없음]
12:00:00.400   1번   [3번]   2번   [4번]
12:00:00.500   3번   [5번]   2번   [4번]
12:00:00.600   5번   [6번]   2번   [4번]
12:00:00.700   5번   [6번]   4번   [없음]
12:00:00.800   6번   [없음]   4번   [없음]
...
12:00:01.100   6번   [없음]   4번   [없음]
12:00:01.200   없음   [없음]   4번   [없음]
12:00:01.300   없음   [없음]   없음   [없음]
1번 요청이 12:00:00.500에 완료됩니다.
따라서 5번 요청은 열려있는 커넥션 수가 더 적은 1번 서버에 할당됩니다.
3번 요청이 12:00:00.600에 완료됩니다.
따라서 6번 요청은 열려있는 커넥션 수가 더 적은 1번 서버에 할당됩니다.
1번 서버는 12:00:01.200에 할당된 요청을 모두 처리하며, 2번 서버는 12:00:01.300에 할당된 요청을 모두 처리합니다.
따라서 모든 요청을 처리한 시각은 12:00:01.300입니다.

Least Connection(12:00:01.300)이 Round Robin(12:00:01.700)보다 0.4초(400ms) 빠르므로 [2, 400]을 반환합니다.
"""
"""
그래프 변형 문제
"""
import datetime


def solution(numServer, logs):
    logs = list(map(lambda i: parse_time(i[0], i[1]), list(map(lambda x: x.split(" "), logs))))
    logs2 = logs.copy()
    round_robin_result = round_robin(numServer, logs)
    least_connection_result = least_connection(numServer, logs2)

    print("round_robin result: {}".format(round_robin_result.time()))
    print("least_connection result: {}".format(least_connection_result.time()))

    time_gap = int(abs(least_connection_result - round_robin_result).total_seconds() * 1000)
    print(time_gap)

    if round_robin_result < least_connection_result:
        return [1, time_gap]
    elif round_robin_result > least_connection_result:
        return [2, time_gap]
    else:
        return [0, 0]


def parse_time(receive_time, required_time):
    parsed_receive_time = datetime.datetime.strptime(receive_time, '%H:%M:%S.%f')
    req_seconds, red_millis = map(lambda x: int(x), required_time.split("."))
    parsed_require_time = datetime.timedelta(seconds=req_seconds, milliseconds=red_millis)

    return (parsed_receive_time, parsed_require_time)


def round_robin(numServer, logs):
    init_time = datetime.datetime.min
    servers_endtime = [init_time for _ in range(numServer)]

    while logs:
        receive_time, required_time = logs.pop(0)
        current_server = len(logs) % numServer
        if servers_endtime[current_server] <= receive_time:
            servers_endtime[current_server] = receive_time + required_time
        else:
            servers_endtime[current_server] += required_time

    return max(servers_endtime)


def least_connection(numServer, logs):
    init_time = datetime.datetime.min
    servers_endtime = [init_time for _ in range(numServer)]

    while logs:
        receive_time, required_time = logs.pop(0)
        current_server = servers_endtime.index(min(servers_endtime))
        if servers_endtime[current_server] <= receive_time:
            servers_endtime[current_server] = receive_time + required_time
        else:
            servers_endtime[current_server] += required_time

    return max(servers_endtime)


logs = ["12:00:00.100 0.400", "12:00:00.200 0.500", "12:00:00.300 0.100", "12:00:00.400 0.600", "12:00:00.500 0.200",
        "12:00:00.600 0.400"]
result = solution(2, logs)
