# 15685 드래곤 커브

#  x 오른쪽, y 아래
# 시작 점, 시작 방향, 세대
# 0세대: 길이: 1인 선분                                     0
# 1세대: 0세대 끝점을 기준으로 90도 회전 후 0세대 끝점에 붙임 0 1
# 2세대: 1세대 끝점을 기준으로 90도 회전 후 1세대 끝점에 붙임 0 1 | 2 1
# 3세대: 2세대 끝점을 기준으로 90도 회전 후 2세대 끝점에 붙임 0 1 2 1 | 2 3 2 1

# 우, 상, 좌, 하, 시계방향: +1 0123
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 입력
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
direction = [[] for _ in range(N)] # 각 드래곤 커브의 방향 저장

# 방향 구하기
for i in range(N):
    x, y, d, g = data[i]
    direction[i].append(d)
    
    for _ in range(g):
        reverse = list(reversed(direction[i]))
        for ele in reverse:
            if ele+1 == 4:
                direction[i].append(0)
            else:
                direction[i].append(ele+1)
        

board = [[0  for __ in range(101)] for _ in range(101)] # 100*100 1일때 꼭짓점이 드레곤 커브의 일부

# 드래곤 커브 이동 값 지도 반영
for i in range(N):
    x, y, d, g = data[i]
    board[y][x] = 1
    for j in direction[i]:
        x, y = x + dx[j], y + dy[j]
        if 0 <= x <= 100 and 0 <= y <= 100:
            board[y][x] = True
    
# 사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수 구하기
answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
            answer += 1

# 출력
print(answer)
