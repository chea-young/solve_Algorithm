# 02294 동전2

# 입력
n, k = map(int, input().split())
data = sorted([int(input()) for _ in range(n)])

dp = [10001] * (k+1)
dp[0] = 0

# 동전의 최소 개수 구하기
for coin in data:
    for i in range(coin, k+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
            
# 만약 가진 동전으로 k 값이 나오지 않는 경우
if dp[-1] == 10001:
    dp[-1] = -1
    
# 출력 
print(dp[-1])
