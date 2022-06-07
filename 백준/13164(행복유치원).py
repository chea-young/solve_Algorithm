# 13164 행복유치원

# N 명을 키 순 일렬, K개의 조
# 한 조에 적어도 한 명
# 같은 조 -> 인접

# 비용 : 큰 원생 - 작은 원생
import sys

# 입력
N, K = map(int, sys.stdin.readline().split())
children = list(map(int, sys.stdin.readline().split()))

# 차이를 빼기
data = []
for i in range(1, N):
    data.append(children[i] - children[i-1])

data.sort(reverse=True)

# 출력
print(sum(data[K-1:]))
