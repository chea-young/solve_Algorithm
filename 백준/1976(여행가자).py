# 여행가자 1976

#입력
N = int(input()) # 도시의 수
M = (input()) # 계획한 속한 도시들의 수
data = [[int(j) for j in input().split()]for i in range(N)]
plan = list(map(int, input().split()))

# 모든 가능한 경로 1로 바꾸기
for connect in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                data[i][j] = 1
            if data[i][connect] == data[j][connect] == 1:
                data[i][j] =1

# 가능한 경로 확인하기
first = plan.pop(0)
state = True
while plan:
    now = plan.pop(0)
    if data[first-1][now-1] != 1:
        state = False
        break
    first = now

# 출력
if state:
    print('YES')
else:
    print('NO')
