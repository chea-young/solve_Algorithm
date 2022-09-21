# 01052 물병
import sys
sys.stdin = open("./백준/input/01052.txt", "r")

"""
N개의 물병 -> 무한대로 가능
초기 1리터 ->K개로 옮기는 것 가능
=> 최소 사야하는 물병 값

 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
 2, 2, 2, 2, 2, 2, 1
 4, 4, 4, 1
 8, 4, 1 -> 1 1 0 1
 => +1
 8, 4, 1 1
 8 4 2 -> 1 1 1 0
 => +1
 8 4 2 1 -> 1 1 1 1
 => +1
 8 4 2 1 1
 8 4 2 2
 8 4 4
 8 8
"""

def input_func():
    input_data = sys.stdin.readline
    N, K = map(int, input_data().split())
    return N, K

def solve(N, K):
    answer = 0

    # 같은 수 2개씩 묶기 -> 이진수로 만들기
    while bin(N).count('1') > K:
        answer += 1
        N += 1
    return answer

#입력
N, K = input_func()

#출력
print(solve(N, K))
