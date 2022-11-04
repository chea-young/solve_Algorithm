# 15828 Router
import sys
from collections import deque
sys.stdin = open("./input/15828.txt", "r")

def input_func():
    input_data = sys.stdin.readline
    N = int(input_data())
    data = []
    while True:
        ele = int(input_data())
        if ele == -1:
            break
        data.append(ele)
    return N, data

def solution(N, data):
    buffer = deque()
    for d in data:
        
        if d == 0: # 패킷 처리
            if buffer:
                buffer.popleft()
        else:
            # 버퍼 공간이 존재할 때만 입력을 받음
            if len(buffer) < N:
                buffer.append(d)
            
    if buffer:
        return buffer
    else:
        return ["empty"]
            

# 입력
N, data = input_func()

# 출력
print(*solution(N, data))
