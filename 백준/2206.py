#벽 부수고 이동하기
global col, row
#아래, 위, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 입력
col, row = map(int, input().split())
data = [[int(j) for j in input()] for i in range(col)]

# 길 찾기 알고리즘
def find_path(data): 
    move = 0
    check_node = [((0, 0), 0)]
    checked_node = []
    while check_node:
        move += 1
        next_check_node = []
        for ele, block in check_node:
            for loc in range(4):
                if 0 <= ele[0] + dy[loc] < col  and 0 <= ele[1] +dx[loc] < row:
                    next = (ele[0] + dy[loc], ele[1] +dx[loc])
                    if next not in checked_node and block + data[next[0]][next[1]]< 2:
                        next_check_node.append(((ele[0]+dy[loc], ele[1]+dx[loc]), block+data[ele[0]+dy[loc]][ele[1]+dx[loc]]))
        checked_node += [i[0] for i in check_node]
        check_node = next_check_node
        
    if (col-1, row-1) in checked_node:
        print(move)
    else:
        print(-1)
find_path(data)
