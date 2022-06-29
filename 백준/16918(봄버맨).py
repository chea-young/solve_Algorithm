# 16918 봄버맨

# 폭탄을 파괴시키는 함수
def destroy_bomb(bombs, R, C):
    destory = set() # 파괴된 폭탄 리스트
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    for y, x in bombs:
        destory.add((y, x))
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < R and 0<= nx < C:
                destory.add((ny, nx))
    return destory

# 입력
R, C, N = map(int, input().split())
miro = []
bombs = [] # 설치된 폭탄의 좌표
for i in range(R):
    data = input()
    miro.append(data)
    for j in range(C):
        if data[j] == 'O':
            bombs.append([i, j])

# N초 동안 격자판 상태 업데이트
all_bomb = [['O' for __ in range(C)]for _ in range(R)] # 모든 것이 폭탄으로 가득한 경우
all_bomb_loc  = set([(i, j)  for i in range(R) for j in range(C)])
if N%2 == 0: 
    # 짝수 초에는 항상 폭탄이 꽉 참
    answer = all_bomb
else:
    for s in range(2, N+1):
        if s%2 == 1: # 3초 전의 설치된 폭탄만 폭발
            # 폭발
            destory = destroy_bomb(bombs, R, C)
            # 현재 설치되어 있는 폭탄 업데이트
            bombs = all_bomb_loc - destory
    answer = [['.' for __ in range(C)]for _ in range(R)]
    for y, x in bombs:
        answer[y][x] = 'O'

# 출력
for ele in answer:
    print(''.join(ele))