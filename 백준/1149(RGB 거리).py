# 1149 RGB거리

# 집 N개, 1-2 다른 색

# 입력
N = int(input())
data = [[int(j) for j in input().split()]for i in range(N)]

for i in range(1, N):
    # min -> 이전 단계에서 자신을 제외한 칩 중의 최솟값 선택
    # min + 자신 -> 해당 단계에서 자신을 골랐을 때
    # red
    data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
    # green
    data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
    #green
    data[i][2] = min(data[i-1][0], data[i-1][1]) + data[i][2]
# 출력
print(min(data[N-1]))
