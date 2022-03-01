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
    
answer = []
check_loc = N-1
check = data.pop()
while data:
    if data[-1] > check:
        answer.append(len(data))
    else:
        ele = 0
        for i in range(len(data)-2, -1, -1):
            if data[i] > check:
                ele = i+1
                break
        answer.append(ele)
    check = data.pop()
answer.append(0)
    
#출력
for i in range(len(answer)-1, -1, -1):
    print(answer[i], end=' ')
                
                
        
        
        
    
