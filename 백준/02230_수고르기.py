# 2230 수열

import sys
import math
sys.stdin = open("./input/2230.txt", "r")

"""
규칙
- 연속된 두일자 일정 1개 이상 -> 일정 연속
- 모든 일정은 하나의 직사겨ㅏㄱ형에 포함
- 가장 작은 직사각형의 크기 만큼 코팅지 오림

+ 일정 -> 시작, 종료 날짜 포함
+ 시작일이 가장 앞선 일정 부터
+ 시작일 동일 -> 일정의 기간이 긴 것
- > 최 상단

==> 코팅지 면적
"""

def input_func():
    input_data = sys.stdin.readline
    N, M = map(int, input_data().split())
    diff= [int(input_data()) for _ in range(N)]
    return N, M, diff

def solution(N, M, diff):
    # 초기 세팅
    diff.sort()
    answer = math.inf
    left = 0
    right = 1
    
    while left < N and right < M:
        ndiff = diff[right] - diff[left]
        if ndiff < M:
            right += 1
        else:
            left += 1
            answer = min(answer, ndiff)
        
        if ndiff == M :
            return M
            
    return answer


def solution_1(N, M, diff):
    # 초기 세팅
    diff.sort()
    answer = math.inf
    for i in range(N-1):
        for j in range(i+1, N):
            ndiff = diff[j] - diff[i]
            if ndiff > answer:
                break
            if ndiff >= M:
                answer = min(answer, ndiff)
                break
        
        if answer == M:
            break

    return answer
            
# 입력
N, M, diff = input_func()

# 출력
print(solution(N, M, diff))
