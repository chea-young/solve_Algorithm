import heapq, sys
INF = sys.maxsize
sys.stdin = open("./input/14938.txt", "r")

def input_func():
    input_data = sys.stdin.readline
    N, M, R = map(int, input().split())

    area_item = list(map(int, input().split()))
    area_item.insert(0, 0)

    route = [ [] for _ in range(N+1)]

    for _ in range(R):
        start, end, dist = map(int, input().split())

        route[start].append([dist, end])
        route[end].append([dist, start])
    return N, M, R, area_item, route

def solve(N, M, R, area_item, route):
    max_value = int(-1e9)
    for i in range(1, N+1):
        temp_sum = 0
        result = dijkstra(i)

        for j in range(1,N+1):
            if result[j] <= M:
                temp_sum += area_item[j]

        max_value = max(max_value, temp_sum)
    return max_value

def dijkstra(S):
    Q = []
    distance = [INF] * (N+1)

    heapq.heappush(Q, [0, S])
    distance[S] = 0

    while Q:
        now_dist, now_vertex = heapq.heappop(Q)

        for next_dist, next_vertex in route[now_vertex]:
            if next_dist + now_dist < distance[next_vertex]:
                next_dist += now_dist
                distance[next_vertex] = next_dist
                heapq.heappush(Q, [next_dist, next_vertex])

    return distance

# 입력
N, M, R, area_item, route = input_func()
print(solve(N, M, R, area_item, route))