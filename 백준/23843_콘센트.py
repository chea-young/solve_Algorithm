#23843 콘센트
import sys
import heapq
sys.stdin = open("./input/23843.txt", "r")

"""

N개의 전자긱 충전 
사용 가능한 콘센트 존재 -> 성능 모두 동일
충전 -> 한 번의 하나의 콘텐트

==> 최소 시간

"""

def input_func():
    input_data = sys.stdin.readline
    N, M = map(int, input_data().split())
    time_info = list(map(int, input_data().split()))
    return N, M, time_info

def solution(N, M, time_info):
    # 초기 세팅
    time_info.sort(reverse = True) # 시간이 많이 필요한 순으로 정렬
    data = []
    
    for ti in time_info:
        if len(data) < M: # 콘센트의 수보다 작은 경우
            heapq.heappush(data, ti) ## heapq는 최소 힙이기 때문에 음수로 넣어주기
        else: # 모든 콘센트가 사용 중인 경우
            ## 현재 상태에서 가장 먼저 끝나는 콘센트에서 다음 충전기 충전
            nsocket = heapq.heappop(data)
            heapq.heappush(data, nsocket+ti)
    
    # 각 콘센트에 사용되는 시간 중 가장 오래걸리는 시간 return
    return max(data)
            

# 입력
N, M, time_info = input_func()

# 출력
print(solution(N, M, time_info))
