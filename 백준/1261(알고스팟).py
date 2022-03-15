# 1261 알고스팟

# 운영진은 모두 같은 방
# 무기 AOJ 부수는 것이 가능 -> 빈 방
#(1, 1) -> (N, M) 최소 몇개 부숴야 하는지!!

import heapq
#입력
N, M = map(int, input().split())
miro = [[int(i) for i in input()] for _ in range(M)]

dy = [-1, 1, 0, 0] # 상 하 좌 우
dx = [0, 0, -1, 1]

visited = [['INF' for __ in range(N)] for _ in range(M)]
check = []

loc = [0, 0]
answer = 0 # 벽부신수
visited[0][0] = 0
heapq.heappush(check, (answer, loc))
while check: # INF 기준으로 고치기
    answer, loc = heapq.heappop(check)
    for i in range(4):
        y = loc[0]+dy[i]
        x = loc[1]+dx[i]
        if 0 <= y < M and 0 <= x < N:
            # INF 이거나 이전의 값보다 현재의 값이 더 적을 때
            if visited[y][x] == 'INF' or visited[y][x] > answer + miro[y][x]: 
                visited[y][x] = answer + miro[y][x]
                heapq.heappush(check, (answer + miro[y][x], [y, x]))  

#출력
print(visited[M-1][N-1])
