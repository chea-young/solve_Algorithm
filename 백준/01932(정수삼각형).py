# 01932 정수 삼각형

# 입력
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dp = [[data[-1][i], i] for i in range(n)] # (값, 인덱스)

# 마지막 줄에서 max 인 수 더하기
for layer in range(len(dp)-2, -1, -1): # 3 2 1 0
    for ele in range(n):
        value, i = dp[ele]
        left = i-1
        right = i
        if left < 0: # 왼쪽 대각선이 없을 때
            left = 0 
        if right >= len(data[layer]): # 오른쪽 대각선이 없을 때
            right = 0
        
        max_num = 0
        max_i = 0
        if data[layer][left] > data[layer][right]:
            max_num = data[layer][left]
            max_i = left
        else:
            max_num = data[layer][right]
            max_i = right
        dp[ele] = [value+max_num, max_i]

# 출력
answer = max([ele[0] for ele in dp])
print(answer)
