# 14466(소가 길을 건너간 이유 6)

"""
K 마리의 소
소는 각자 다른 목초지
길을 건너지 X 못 만남



"""


import sys
from collections import deque

# 입력
N, K, R = map(int, input().split())
road = [[[] for _ in range(N+1)] for _ in range(N+1)]

for i in range(R):
    r,c,rr,cc = map(int, sys.stdin.readline().split())
    road[r][c].append([rr,cc])
    road[rr][cc].append([r,c])

cow_map = [[False for _ in range(N+1)] for _ in range(N+1)]
cow_list = []
for i in range(K):
    r, c = map(int, sys.stdin.readline().split())
    cow_list.append([r,c])
    cow_map[r][c] = True

# 상하좌우 이동 정보
dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 길 없이 이동할 수 있는 소 찾기
result = 0
for r,c in cow_list:
    if cow_map[r][c]: # 중복된 소가 아닌 경우
        visited = [[True for _ in range(N+1)] for _ in range(N+1)]
        check = deque()
        check.append([r,c])
        cow_map[r][c] = False
        cnt = 0
        K -= 1 # 이전에 다른 소들은 한번씩 확인을 했기 때문에
        while check:
            y,x = check.popleft()
            for u in range(4):
                yy = y + dy[u]
                xx = x + dx[u]
                if 1<=yy<=N and 1<=xx<=N and visited[yy][xx]:
                    if [yy,xx] not in road[y][x]: # 이동할 때 길이 아닌 경우
                        check.append([yy,xx])
                        visited[yy][xx] = False
                        if cow_map[yy][xx]: # 현재 위치에 소가 있는 경우
                            cnt += 1
        result += K-cnt
print(result)