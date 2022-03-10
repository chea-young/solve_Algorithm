# 1009 분산처리

#입력
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print((a**b)%10) # 출력
