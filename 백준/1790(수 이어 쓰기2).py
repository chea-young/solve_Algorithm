# 수 이어 쓰기 2 - 1790

# 입력
N, k = map(int, input().split())

# 이어진 숫자 list 만들기
data = ''
for i in range(1, N+1):
    data += str(i)
    
#출력
try:
    print(data[k-1])
except IndexError:
    print(-1)
