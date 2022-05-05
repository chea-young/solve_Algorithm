# 나이트의 이동 7562
from collections import deque

dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]

def bfs(l, now_loc, dest_loc):
    visited = [[-1 for __ in range(l)] for _ in range(l)]
    queue = deque()
    queue.append([now_loc, 0]) # 위치, 이동 횟수
    visited[now_loc[0]][now_loc[1]] = 0
    while queue:
        loc, count = queue.popleft()
        for i in range(8):
            x = dx[i] + loc[0]
            y = dy[i] + loc[1]
            if 0 <= x < l and 0 <= y < l and visited[x][y] == -1:
                queue.append([(x,y), count+1])
                visited[x][y] = count + 1
    return visited[dest_loc[0]][dest_loc[1]]
                    

# 입력
test_cnt = int(input())
for _ in range(test_cnt):
    l = int(input())
    now_loc = list(map(int, input().split()))
    dest_loc = list(map(int, input().split()))
    
    # 출력
    print(bfs(l, now_loc, dest_loc))
