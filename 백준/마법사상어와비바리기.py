n, m = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(n)]
moves = []
for i in range(m):
    tmp = list(map(int, input().split()))
    moves.append([tmp[0] - 1, tmp[1]])

clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 비바라기 시전
for i in range(m):
    ## step 1. 이동
    move = moves[i]
    nextClouds = []
    for cloud in clouds:
        x = cloud[0]
        y = cloud[1]
        d = move[0]
        s = move[1]
        nx = (x+dx[d]*s)%n
        ny = (y+dy[d]*s)%n
        nextClouds.append([nx, ny])

    ## step 2. 물 증가하기
    visited = [[False]* n for _ in range(n)]
    for cloud in nextClouds:
        x = cloud[0]
        y = cloud[1]
        arr[x][y] += 1
        visited[x][y] = True
    
    # step 3 구름 비우기
    clouds = []

    # step 4  대각선 방향으로 물이 존재하면 추가하기
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for cloud in nextClouds:
        x = cloud[0]
        y = cloud[1]
        count = 0
        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]

            if 0 <= nx < n and 0<= ny < n and arr[nx][ny] >= 1:
                count += 1

        arr[x][y] += count
        
    # step 5 물의 양이 2개 이상인 곳에 구름 생성시키기
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and visited[i][j] == False:
                arr[i][j] -= 2
                clouds.append([i, j])

# 전체 최종 물의 양 구하기
ans = 0
for i in range(n):
    ans += sum(arr[i])

# 출력
print(ans)