# 토마토
# 입력
row, col = map(int, input().split())
data = [[int(j) for j in input().split()] for i in range(col)] 

day = 0
checked = [] # 이미 주변을 1로 만든 토마토를 넣는 list
check = [] # 주변을 1로 만들 토마토를 넣는 list
for c in range(col): # find 익은 토마토
    for r in range(row):
        if data[c][r] == 1 and (c, r) not in checked:
            check.append((c,r))

while True:                
    if check == []: # 1로 만들 토마토가 없을 경우 while loop 종료
        break
    next_check = [] 
    for now_index in check: # 왼, 오, 앞, 뒤 1로 만들기
        #left
        if now_index[1]-1 >= 0 and data[now_index[0]][now_index[1]-1] == 0:
            data[now_index[0]][now_index[1]-1] = 1
            next_check.append((now_index[0], now_index[1]-1))
        # right
        if now_index[1]+1 != row and data[now_index[0]][now_index[1]+1] == 0:
            data[now_index[0]][now_index[1]+1] = 1
            next_check.append((now_index[0], now_index[1]+1))
        # front
        if now_index[0]-1 >= 0 and data[now_index[0]-1][now_index[1]] == 0:
            data[now_index[0]-1][now_index[1]] = 1
            next_check.append((now_index[0]-1, now_index[1]))
        # back
        if now_index[0]+1 != col and data[now_index[0]+1][now_index[1]] == 0:
            data[now_index[0]+1][now_index[1]] = 1
            next_check.append((now_index[0]+1, now_index[1]))
    checked +=  check
    check = next_check
    day += 1

state = True
for ele in data:
    if 0 in ele: 
        state = False
        break
if state:
    print(day-1)
else:
    print(-1)
