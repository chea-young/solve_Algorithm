# 18869 멀티버스2

"""
환승  - 최소
출발역; 서울역 : 0
호선: 역의 집합
역: 정점

!! 최소 환승 수


"""
import sys

def input_data():
    input_func = sys.stdin.readline
    N = int(input_func())
    line_list = [list(map(int, input_func().split())) for _ in range(N)]
    destination = int(input_func())
    return N, line_list, destination

def solve(N, line_list, destination):
    global check_station, check_line, answer

    # 초기 설정
    start = 0 # 시작은 항상 서울역
    check_station = [0] # 탐색한 역
    check_line = [0] * N # 탐색한 역
    answer = 10
    now_line = 0

    # 역 연결 정보 만들기
    linked_station = {} # station: [station, line]

    for i in range(N):
        for s in range(len(line_list[i])):
            ns = line_list[i][s]
            if ns == 0:
                now_line = s
            
            # 전 역
            if s > 0:
                linked_station[ns] = linked_station.get(ns, []) + [[line_list[i][s-1], i]]

            # 다음 역
            if s < len(line_list[i]) - 1:
                linked_station[ns] = linked_station.get(ns, []) + [[line_list[i][s+1], i]]
    print(linked_station)
    #find_transfer_cnt(0, 0, now_line) # 현재 역, 환승횟수

    return answer


def find_transfer_cnt(now_station, transfer_cnt, now_line):
    global check_station, check_line, answer

    if now_station == destination: # 목적지에 도착한 경우
        answer = min(answer, transfer_cnt)

    if transfer_cnt > answer: # 현재 환승 수가 이전의 최소 환승 수보다 큰 경우
        return
    
    for i in range(N):
        if check[i]: # 이미 환승했던 호선인 경우
            continue





# 입력
N, line_list, destination = input_data()

# 출력
print(solve(N, line_list, destination))