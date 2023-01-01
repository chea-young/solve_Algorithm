"""
지도 - 바다, 무인도 표시
 - X or 숫자

sum (상하좌우) = 머물 수 있는 척도

지낼 수 있는 무인도 X -> -1


"""
from collections import deque

def solution(maps):
    global map_list, col, row
    
    # 초기 설정
    answer = []
    col, row = len(maps), len(maps[0])
    map_list = [list(i) for i in maps]
    
    # 각 섬에서 머물 수 있는 수 구하기
    for y in range(col):
        for x in range(row):
            if map_list[y][x] != 'X':
                cnt  = sum_island([y, x])
                if cnt: ## 해당 섬이 머물 수 있는 섬인 경우 -> 배열에 추가
                    answer.append(cnt)
    
    # 머물 수 있는 섬이 존재하는지 확인
    if not answer:
        return [-1]
    return sorted(answer)

def sum_island(now):
    global map_list, col, row
    
    # 초기 설정
    dy = [-1,1, 0, 0]
    dx = [0, 0, -1, 1]
    check = deque() # [(y좌표, x좌표)]
    cnt = 0
    
    # 머물 수 있는 수 구하기
    check.append(now) 
    cnt = int(map_list[now[0]][now[1]])
    map_list[now[0]][now[1]] = 'X'
    while check:
        ny, nx = check.popleft()
        
        for i in range(4):
            nny = ny + dy[i]
            nnx = nx + dx[i]
            
            ## 좌표가 map 범위 안이고, 다음 위치가 숫자인 경우
            if 0<=nny<col and 0<=nnx<row and map_list[nny][nnx].isdigit():
                cnt += int(map_list[nny][nnx])
                map_list[nny][nnx] = 'X'
                check.append([nny, nnx])
    return cnt

print(solution(["X591X","X1X5X","X231X", "1XXX1"])) # [1, 1, 27]
print(solution(["XXX","XXX","XXX"])) # [-1]
