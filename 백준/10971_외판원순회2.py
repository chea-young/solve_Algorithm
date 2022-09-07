import sys
sys.stdin = open("./input/10971.txt", "r")

def dfs(cnt, next, value):
    global min_value

    if cnt == N-1:
        if travel[next][0] != 0:
            min_value = min(min_value, value + travel[next][0])
        return

    for i in range(N):
        if travel[next][i] != 0 and i != 0:
            if visited[i]:
                continue

            visited[i] = 1
            dfs(cnt+1, i, value + travel[next][i])
            visited[i] = 0

N = int(input())
travel = [list(map(int, input().split())) for _ in range(N)]

min_value = sys.maxsize

global visited
visited = [0] * N
visited[0] = 1

dfs(0, 0, 0)

print(min_value)