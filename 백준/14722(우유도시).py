# 14722 우유도시

# 처음 딸기 우유
# 딸기 -> 초코
# 초코 -> 바나나
# 바나나 -> 딸기

# 시작 -> 1,1
# 이동 -> 동쪽, 남쪽
from collections import deque

# 입력
N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1]
dy = [1, 0]
mikes = [0, 1, 2] # 딸기, 초코, 바나나

data = deque()
answer = 0
data.append(((0, 0), 1)) # 현재 좌표, 우유 개수
while data:
    nowLoc, nowMove = data.popleft()
    newMilk = mikes[(nowMove)%3]
    for i in range(2):
        nx = dx[i] + nowLoc[0]
        ny = dy[i] + nowLoc[1]
        if 0 <= nx < N and 0 <= ny < N and city[ny][nx] == newMilk:
            if answer < nowMove + 1:
                answer = nowMove + 1
            data.append(((nx, ny), nowMove+1))
            

# 출력
print(answer)
