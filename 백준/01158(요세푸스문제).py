# 01158 요세푸스 문제

# N명 
# K 번째 사람 제거

# 입력
N, K = map(int, input().split())
answer = []
data = [i+1 for i in range(N)]
now = 0
while data:
    now += K-1
    now = now%len(data)
    answer.append(data[now])
    del data[now]

# 출력
print(f'<{", ".join(map(str, answer))}>')
