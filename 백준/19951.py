# 19951 태상이의 훈련소 생활

"""
연변장: N개 칸
a ~ b 까지 k 높이
-> 최종 높이를 미리 구해 한번에 일 수행

order
- a ~ b 까지 K만큼


0 0 0 0 0 0 0 0 0 0 0
-3 0 0 0 0 3 0 0 0 0 0
"""
import sys


def input_data():
    input_func = sys.stdin.readline
    N, M = map(int, input_func().split())
    height_list = list(map(int, input_func().split()))
    order_list = [list(map(int, input_func().split())) for _ in range(M)]
    return N, M, height_list, order_list

def solve(N, M, height_list, order_list):
    # init
    cal_order_list = [0] * (N+1) # 현재 추가해야 되는 땅의 값을 저장하는 리스트 (N+1: 만약에 N까지 수행해야하는 경우를 대비)
    
    # get cal_order_list
    for a, b, k in order_list:
        cal_order_list[a-1] += k
        cal_order_list[b] -= k
        
    # get total height
    soil = 0
    for i in range(N):
        soil += cal_order_list[i]
        height_list[i] += soil
    
    return height_list
        
# 입력
N, M, height_list, order_list = input_data()

# 출력
print(*solve(N, M, height_list, order_list))