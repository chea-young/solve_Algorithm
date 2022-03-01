# 탑 2493

# N개 높이 탐 왼쪽-> 오른쪽 세우고
# 각 꼭대기 송신기 설치
# 레이저 신호를 수평 직선의 왼쪽 방향으로 발사
# 나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신

# 입력
N = int(input())
data = []
for i in input().split():
    data.append(int(i))
# 탑 순서 구하기
stack = [[1, data[0]]]
answer = [0]
for i in range(1, N):
    while stack:
        if stack[-1][1] > data[i]:
            answer.append(stack[-1][0])
            stack.append([i+1, data[i]])
            break
        else:
            stack.pop()
    
    if not stack:
        answer.append(0)
        stack.append([i+1, data[i]])    
#출력
for i in answer:
    print(i, end=' ')
