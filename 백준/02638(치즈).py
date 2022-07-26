# 02638 치즈

# 한시간 내로 녹아 없어지는 치즈 찾기
def find_cheeze(board, cheeze):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    destory = set()
    for i, j in cheeze:
        cnt = 0
        for n in range(4):
            ny = dy[n] + i
            nx = dx[n] + j
            if not board[ny][nx]: # 벽인 경우
                cnt += 1
    
        # 2면이상 공기에 접촉하고 있을 때
        if cnt >= 2:
            destory.add((i, j))
    return destory

# 치즈 녹이기
def melt_cheeze(board, destory):
    for i, j in destory:
        board[i][j] = 0
    return board

# 입력
N, M = map(int, input().split())
board = []
cheeze = set()
for i in range(N):
    ele = list(map(int, input().split()))
    for j in range(M):
        if ele[j]:
            cheeze.add((i, j))
    board.append(ele)

answer = 0
while cheeze:
    answer += 1
    destory = find_cheeze(board, cheeze)
    board = melt_cheeze(board, destory)
    cheeze -= destory # 한 시간 후 삭제하기

# 출력
print(answer)
