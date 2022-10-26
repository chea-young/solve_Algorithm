# 11000 강의실 배정

import sys
import heapq

"""

정렬된 timetable을 for문을 돌면서 
    lecture[0] 보다 S가 크거나 같으면 
        while lecture[0] > S 때까지 pop 진행하고
        마지막에 push
    lecture[0] 보다 S가 작으면 push
"""

def input_Data():
    input = sys.stdin.readline
    N = int(input())
    timetable = [list(map(int, input().split())) for _ in range(N)]
    return N, timetable

def solution(N, timetables):
    #초기 설정
    timetable.sort()
    lecture = [] # 끝나는 시간을 넣는 함수
    answer = 0
    
    # 최소 강의실 수 찾기
    for s, t in timetables:
        ## 사용하고 있던 강의실 수업이 끝난 경우
        while lecture and lecture[0] <=s:
            heapq.heappop(lecture) ### 강의실 회수
        
        ## 현재 수업 강의실 사용하기
        heapq.heappush(lecture, t)
        answer = max(answer, len(lecture))
    return answer
    
# 입력
N, timetable = input_Data()

#출력
print(solution(N, timetable))
