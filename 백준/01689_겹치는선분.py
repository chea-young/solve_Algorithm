# 01689 겹치는 선분
import sys
import heapq
sys.stdin = open("./백준/input/01689.txt", "r")

def input_func():
    input_data = sys.stdin.readline
    N = int(input_data())
    lines = [list(map(int, input_data().split())) for _ in range(N)]
    return N, lines

def solve_1(N, lines):
    # 초기설정
    lines.sort()
    data = []
    answer = 0

    heapq.heappush(data, lines[0][1])
    cnt = 1
    for s, e in lines[1:]:
        while data and data[0] <= s: # 선분이 겹칠 수 없는 경우
            heapq.heappop(data)
        
        heapq.heappush(data, e)
        answer = max(answer, len(data))

    return answer

def solve(N, lines):
    # 초기설정
    lines.sort()
    data = []
    answer = 0

    cnt = 1
    start, end = 0, 0
    for s, e in lines:
        if s < end: # 겹치는 선분인 경우
            cnt += 1
        else: # 겹치지 않는 선분인 경우
            start, end = s, e
            cnt = 1
        answer = max(cnt, answer)

    return answer

#입력
N, lines = input_func()

#출력
print(solve(N, lines))
