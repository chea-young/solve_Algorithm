#05972 택배 배송

from collections import deque
# 입력
N, M = map(int, input().split())

# 연결 정보 구하기
conn = {i+1:[] for i in range(N)} # 헛간: [(연결된 헛간, 소), ...]
visited = [False for _ in range(N+1)]
for ele in range(M):
    node1, node2, weight = map(int, input().split())
    conn[node1].append([node2, weight])
    conn[node2].append([node1, weight])

queue = deque()
queue.append((1, 0)) # 헛간, 소
visited[1] = 0
while queue:
    check = queue.popleft()
    for ele in conn[check[0]]:
        new_weight = check[1] + ele[1]
        if not visited[ele[0]]:
            visited[ele[0]] = new_weight
            queue.append([ele[0], new_weight])
        else:
            if visited[ele[0]] > new_weight: 
                visited[ele[0]] = new_weight
                queue.append([ele[0], new_weight])

#출력
print(visited[-1])
