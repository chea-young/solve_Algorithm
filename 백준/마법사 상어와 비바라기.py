# 21610 마법사 상어와 비바라기

"""

파이어볼, 토네이도, 파이어스톰, 물복시 버그 !!비바라기

r, c 물의 양

 (N, 1), (N, 2), (N-1, 1), (N-1, 2) -> 비구름
 사라짐

1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
- 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
- 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.

# CHECK 수정하기
"""

# 입력
N, M = map(int, input().split())
nList = [ list(map(int, input().split())) for _ in range(N)]
mList = [ list(map(int, input().split())) for _ in range(M)]

## 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [(N, 1), (N, 2), (N-1, 1), (N-1, 2)]

# 비바라기 시전
for d, s in mList:
    ## 이동하기
    moveCloud = []
    for ele in cloud:
        y, x = ele
        # 행으로 이동
        y = (y+dy[d-1]*s)%N
        # 열으로 이동
        x = (x+dx[d-1]*s)%N
        moveCloud.append((y, x))
            
    
    ## 물 증가하기
    for y, x  in moveCloud:
        nList[y][x] += 1
    
    ## 대각선 방향으로 물이 존재하면 추가하기
    for y, x in moveCloud:
        cnt = 0 # 주변에 있는 물의 수
        for i in range(4):
            ny = dy[2*i+1] + y
            nx = dx[2*i+1] + x
            if 0<=ny<N and 0<=nx<M and nList[ny][nx]>0:
                cnt += 1
        nList[y][x] += cnt

    ## 물의 양이 2개 이상인 곳에 구름 생성시키기
    nextCloud = set()
    for i in range(N):
        for j in range(N):
            if nList[i][j]>= 2:
                nextCloud.add((i, j))
                nList[i][j] -= 2
    cloud = nextCloud - set(moveCloud)

# 전체 최종 물의 양 구하기
ans = 0
for i in range(N):
    ans += sum(nList[i])

# 출력
print(ans)