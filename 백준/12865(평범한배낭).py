# 12865 평범한 배낭

# 입력
N, K = map(int, input().split())
data = [ [int(j) for j in input().split()] for i in range(N)]

dp = [0]*(K+1) # 0부터 K 무게까지 저장
for i in range(K+1):
    for ele in data:
        if i-ele[0] >= 0:
            dp[i] = max(dp[i], dp[i-ele[0]]+ele[1])

# 출력
print(dp[-1])
