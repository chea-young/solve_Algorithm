import sys
import heapq
sys.stdin = open("./input/14938.txt", "r")
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(S):
    Q = []
    distance = [INF] * (N+1) #  현재 시작하는 지역부터 확인하는 지역까지의 거리 값이

    heapq.heappush(Q, [0, S]) # 현재 아이템 수, 시작지역 
    distance[S] = 0

    while Q:
        now_dist, now_vertex = heapq.heappop(Q)

        for next_dist, next_vertex in arr[now_vertex]:
            if next_dist + now_dist < distance[next_vertex]:
                next_dist += now_dist
                distance[next_vertex] = next_dist
                heapq.heappush(Q, [next_dist, next_vertex])

    return distance

# 입력
N, M, R = map(int, input().split())

area_item = [0]+list(map(int, input().split()))

arr = [ [] for _ in range(N+1)] # 각 인덱스가 자신과 연결된 것.
for _ in range(R):
    start, end, dist = map(int, input().split())
    arr[start].append([dist, end])
    arr[end].append([dist, start])

max_value = int(-1e9)
print(max_value)
for i in range(1, N+1):
    temp_sum = 0
    result = dijkstra(i)
    
    for j in range(1,N+1):
        if result[j] <= M:
            temp_sum += area_item[j]
    max_value = max(max_value, temp_sum)

print(max_value)