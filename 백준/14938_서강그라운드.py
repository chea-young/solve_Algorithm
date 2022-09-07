import sys
import heapq
sys.stdin = open("./input/14938.txt", "r")

def input_func():
    readl = sys.stdin.readline
    N, M, R = map(int, readl().split())
    items = list(map(int, readl().split()))
    locals_info = [list(map(int, readl().split())) for _ in range(R)]
    return N, M, R, items, locals_info

def solve(N, M, R, items, locals_info):
    # 초기 세팅
    global route
    route = {i:[] for i in range(1, N+1)}
    for l1, l2, dis in locals_info:
        route[l1].append([l2, dis])
        route[l2].append([l1, dis])

    data = []
    max_value = 0

    # 최대 개수 찾기
    for i in range(1, N+1):
        result = dijkstra(i)
        max_value = max(max_value, result)
    return max_value

def dijkstra(start):
    # 초기세팅
    global route
    data = [] # -최대 아이템수, 지역, 수색범위
    visited = [1] * (N+1)
    sum_list = [0] * (N+1)
    
    result = 0
    heapq.heappush(data, [-items[start-1], start, 0]) 
    visited[start] = -items[start-1]
    sum_list[start] = items[start-1]
    while data:
        now_cnt, now_local, now_dis = heapq.heappop(data)
        for l, dis in route[now_local]:
            next_cnt = now_cnt-items[l-1]
            next_dis = now_dis + dis

            # 수색 범위를 벗어나는 경우
            if next_dis > M:
                continue
            
            # 데이터를 업데이트 가능한 경우
            if visited[l] == 1 or visited[l] >= next_cnt:
                visited[l] = next_cnt
                sum_list[l] = items[l-1]
                heapq.heappush(data, [next_cnt, l, next_dis])

    return sum(sum_list)

# 입력
N, M, R, items, locals_info = input_func()

print(solve(N, M, R, items, locals_info))