# 3190 뱀

# 사과 먹으면 -> 길이가 늘어남
# 벽 or 자기 자신과 충돌 -> death
# 시작위치 (0, 0)/ 길이 1 / 오른쪽
# L: 왼쪽, D:오른쪽

## 이동
# 머리를 다음칸 위치
# 사과 0, 사과가 없어지고 꼬리 이동X
# 사과 X, 길이 줄이고 꼬리가 위치한 칸 비워짐

# 입력
N = int(input())
apple_num = int(input())
apple_loc = [list(map(int, input().split())) for _ in range(apple_num)]
snake_d_cnt = int(input())
snake_d_info = [input().split() for _ in range(snake_d_cnt)] 

board = [[0 for __ in range(N)] for _ in range(N)] # 사과 있는 곳은 A, 뱀, S
for ele in apple_loc:
    board[ele[0]-1][ele[1]-1] = 'A'
dn = [(0, 1), (1, 0), (0, -1), (-1, 0)] # D: +1, L: -1

second = 0
d = 0
head = [0, 0]
tail = [0, 0]
go = [[0, 0]] # 뱀이 가는 곳을 순서대로 넣은 것
board[0][0] = 'S'
while True:
    second += 1
    # 머리 이동 하기
    next_head = [head[0]+dn[d][0], head[1]+dn[d][1]]
    #print(next_head, board[next_head[0]][next_head[1]])
    if 0 <= next_head[0] < N and 0 <= next_head[1] < N: # 벽인지, 몸인지 확인
        head = next_head
        go.append(head)
    else:
        break
    
    # 사과 확인
    if board[head[0]][head[1]] != 'A':
        board[tail[0]][tail[1]] = 0
        tail = go.pop(0)
    
    # 꼬리 이동 후 몸일때
    if board[head[0]][head[1]] == 'S':
        break
    
    board[head[0]][head[1]] = 'S'
    
    # 뱀의 방향 변화 정보 비교
    if snake_d_info != [] and int(snake_d_info[0][0]) == second:
        next_d = snake_d_info.pop(0)
        if next_d[1] == 'D':
            d += 1
            if d == 4: d = 0
        else:
            d -= 1
            if d == -1: d = 3
# 출력
print(second)
