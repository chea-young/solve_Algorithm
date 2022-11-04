# 11399 ATM
import sys
from collections import deque
sys.stdin = open("./input/11399.txt", "r")

def input_func():
    input_data = sys.stdin.readline
    N = int(input_data())
    people = list(map(int, input_data().split()))
    return N, people
    

def solution(N, people):
    people.sort()
    answer = 0
    pre = 0
    for p in people:
        answer += pre + p
        pre += p
    return answer

# 입력
N, people = input_func()


# 출력
print(solution(N, people))
