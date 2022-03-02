# 적록색약 10026

# 빨강, 초록 유사
# 상하좌우 인접 경우 두글자는 같은 구역 RG
# 아닌사람 적록석약 사람

def bfs(c, r, visited, data):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [(c, r, data[c][r])]
    visited[c][r] = 1
    while queue:
        check = queue.pop(0)
        for i in range(4):
            ny = check[0] + dy[i]
            nx = check[1] + dx[i]
            if -1 < nx < N and -1 < ny < N:
                if visited[ny][nx] == 0  and check[2] == data[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append((ny, nx, check[2]))
    return visited

# 입력
N = int(input())
rg = []
not_rg = []
for i in range(N):
    ele = input()
    ele_1 = []
    ele_2 = []
    for j in ele:
        ele_1.append(j)
        if j in ['R', 'G']:
            j = 'RG'
        ele_2.append(j)
    rg.append(ele_2)
    not_rg.append(ele_1)

rg_visited = [[0 for j in range(N)]for i in range(N)]
rg_space = 0
# 적록색약일 때
for c in range(N):
    for r in range(N):
        if rg_visited[c][r] == 0:
            rg_space += 1
            rg_visited = bfs(c, r, rg_visited, rg)
 
not_rg_visited = [[0 for j in range(N)]for i in range(N)]
not_rg_space = 0
# 적록색약이 아닐 때
for c in range(N):
    for r in range(N):
        if not_rg_visited[c][r] == 0:
            not_rg_space += 1
            not_rg_visited = bfs(c, r, not_rg_visited, not_rg)
# 출력
print(not_rg_space, rg_space)
