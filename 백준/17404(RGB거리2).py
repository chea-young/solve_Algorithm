#17404 RGB거리 2

# 연속으로 다른 색 -> 원형!!
# 맨 처음과 끝이 달라야 한다.

# 입력
N = int(input())
data = [[int(j) for j in input().split()]for i in range(N)]

answer = 1001
for initcolor in range(3): # 첫 번째 색이 정해진 상태
    dp = [[0 for j in range(3)]for i in range(N)]    

    # 2번째 채우기
    for i in range(3):
        if initcolor == i:
            dp[1][i] = 1001
            continue# 선택이 안되게 하기 위해서
        dp[1][i] = data[0][initcolor] + data[1][i]
        
    # 3 - N-1번째까지 채우기
    for i in range(2, N-1):
        # min -> 이전 단계에서 자신을 제외한 칩 중의 최솟값 선택
        # min + 자신 -> 해당 단계에서 자신을 골랐을 때
        # red
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0]
        # green
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + data[i][1]
        # blue
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + data[i][2]
    
    # 마지막 채우기
    for i in range(3):
        if initcolor == i: # 첫번째와 이전이 같을 때
            dp[N-1][i] = 1001 # 선택이 안되게 하기 위해서
            continue
        dp[N-1][i] = min(dp[N-2][(i+1)%3], dp[N-2][(i+2)%3]) + data[N-1][i]
    answer = min(answer, min(dp[N-1]))

# 출력
print(answer)
