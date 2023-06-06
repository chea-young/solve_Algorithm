
# 27311 

"""
크림 하트 판별

#: 크림
.: 크림 없음

확인 조건
1. 덩어리가 한 개인가
2. 하나의 덩어리에 구명이 있지 않는가?
3. N, M의 정사각형
    - 4 방향으로 정사각형 구명이 있는지 확인
    
1. minWidth minHeight maxWidth maxHeight 찾으면서 #.# -> 면 false
2. 가로로 모두 확인, 세로로 모두 확인
"""
import sys


def input_data():
    input_func = sys.stdin.readline
    R, C = map(int, input_func().split())
    latte = [list(input_func().split()) for _ in range(R)]
    return R, C, latte

def solve(R, C, latte):
    # init
    for i in range (R):
        for j in range(C):
            


T = int(input())
for _ in range(T):
    # 입력
    R, C = input_data()

    # 출력
    print(solve(R, C))