# 14891 톱니바퀴

"""
톱니 - 0N, 1S 
K번 회전
회전 - 시계, 반시계

맞닿은 극이 다르면  - 반대방향으로 회전

"""
# 기어를 돌리는 함수
def roate_gear(g, n):
    if n > 0: # 시계방향
        return g[-1] + g[:-1]
    else: # 반시계방향
        return g[1:] + g[0]

# 입력
gear = [input() for _ in range(4)]
K = int(input())
rotation = [list(map(int, input().split())) for _ in range(K)]

# 회전 시키기
for g, n in rotation:

    # 왼쪽으로 확인
    pre_state = gear[g-1][6]
    now_n = n
    for i in range(g-1, 0, -1):
        now_state = gear[i-1][2]
        if pre_state == now_state:
            break
        else:
            pre_state = gear[i-1][6]
            now_n *= (-1)
            gear[i-1] = roate_gear(gear[i-1], now_n)

    # 오른쪽으로 확인
    pre_state = gear[g-1][2]
    now_n = n
    for i in range(g+1, 5):
        now_state = gear[i-1][6]
        if pre_state == now_state:
            break
        else:
            pre_state = gear[i-1][2]
            now_n *= (-1)
            gear[i-1] = roate_gear(gear[i-1], now_n)

    # 현재 회전
    gear[g-1] = roate_gear(gear[g-1], n)

# 점수 계산하기
answer = 0
for i in range(4):
    if gear[i][0] == '1':
        answer += 2**i
            
# 출력
print(answer)