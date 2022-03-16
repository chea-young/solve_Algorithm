#색칠하기 13265

from collections import deque
import sys

def bfs(x):
    global answer	
    check.append(x)
    circle[x] = 1 # 색은 1, -1
    color = -1
    while check:
        now = check.popleft() # 현재 탐색하는 원
        color = circle[now] * (-1)
        for i in data[now]:
            if circle[i] == 0:
                circle[i] = color
                check.append(i)
            else:
                if circle[now] == circle[i]:
                    answer = 'impossible'
        if answer == 'impossible': break

# 입력
T = int(input())
for _ in range(T):
    c, l = map(int, sys.stdin.readline().split())
    circle = [0] * (c+1)
    data = [[] for i in range(c+1)]
    # 양방향으로 데이터 받기
    for i in range(l):
        x, y = map(int, sys.stdin.readline().split())
        data[x].append(y)
        data[y].append(x)
    answer = 'possible'
    check = deque()
    bfs(1)

	# 색칠 안된 것들도 있을 수 있으니 한번 더 bfs탐색 
    for i in range(c+1):
        if circle[i] == 0:
            bfs(i)
    print(answer) #출력
