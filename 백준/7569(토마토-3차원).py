# 7569 토마토

# 익은 토마토 인접 -> 익음! 
# 위 아래 왼쪽 오른쪽 앞 뒤
# 1 -> 익은 0 -> 익지 X, -1 -> 없는 거
# 최소 일 수!!

# 입력
M, N, H = map(int, input().split())
boxes = []
check = [] # 하루에 익어야하는 토마토들
visited = [[[0 for _ in range(M)] for __ in range(N)] for _ in range(H)]
for h in range(H):
    data = []
    for n in range(N):
        ele = []
        word = input().split()
        for m in range(M):
            ele.append(int(word[m]))
            if word[m] == '1' :
                check.append([h, n, m])
                visited[h][n][m] = 1
        data.append(ele)
    boxes.append(data)       
            
# 위 아래 왼쪽 오른쪽 앞 뒤
d = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
answer = -1 # 날짜! -> 첫날부터 +1이 되기 때문에 
while check:
    answer += 1
    next_check = []
    while check:
        now = check.pop(0)
        for move in d: # 위 아래 왼쪽 오른쪽 앞 뒤 -> 확인
            z = now[0] + move[0]
            y = now[1] + move[1]
            x = now[2] + move[2]
            if 0 <= z < H and 0 <= y < N and 0 <= x < M and visited[z][y][x] == 0:
                visited[z][y][x] = 1
                if boxes[z][y][x] == 0:
                    boxes[z][y][x] = 1
                    next_check.append([z, y, x])
    check = next_check
    
# 다 익었는지 확인
count = 0
for data in visited:
    for ele in data:
        count += sum(ele)
# 출력
if count == H*N*M:
    print(answer)
else:
    print(-1)
