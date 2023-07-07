"""
N
1번 -> 번호 증가
마지막 -> 1번
1초 -> 다음 음식 (가장 가까운 번호 음식)

"""
import heapq

def solution(food_times, k):
    
    # data 정리
    data = [] #round, order, time
    for f in range(len(food_times)):
        heapq.heappush(data, [0, f, food_times[f]])
    
    # k초 전까지 음식 섭취
    for i in range(0, k):
        if not data: # 섭취할 음식이 없는 경우
            return -1 
        now_round, now_order, now_time = heapq.heappop(data)
        if now_time - 1 > 0:
            heapq.heappush(data, [now_round+1, now_order, now_time-1])
            
    # k초 후에 섭취할 음식 찾기
    answer = heapq.heappop(data)
    return answer[1]+1


"""
food_times=[4,2,3,6,7,1,5,8] k=16 answer = 3
food_times=[4,2,3,6,7,1,5,8] k=27 answer = 5
"""