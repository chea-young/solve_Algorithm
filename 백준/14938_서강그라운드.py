import heapq, sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(S):
    Q = []
    distance = [INF] * (N+1)

    heapq.heappush(Q, [0, S])
    distance[S] = 0

    while Q:
        now_dist, now_vertex = heapq.heappop(Q)

        for next_dist, next_vertex in arr[now_vertex]:
            if next_dist + now_dist < distance[next_vertex]:
                next_dist += now_dist
                distance[next_vertex] = next_dist
                heapq.heappush(Q, [next_dist, next_vertex])

    return distance

N, M, R = map(int, input().split())

area_item = list(map(int, input().split()))
area_item.insert(0, 0)

arr = [ [] for _ in range(N+1)]

for _ in range(R):
    start, end, dist = map(int, input().split())

    arr[start].append([dist, end])
    arr[end].append([dist, start])

max_value = int(-1e9)

for i in range(1, N+1):
    temp_sum = 0
    result = dijkstra(i)

    for j in range(1,N+1):
        if result[j] <= M:
            temp_sum += area_item[j]

    max_value = max(max_value, temp_sum)

print(max_value)