# 19598 최소 회의실 개수

"""
1. 회의실 정보를 시작하는 시각을 기준으로 정렬
2. for문을 돌면서 now_room 리스트를 끝나는 시각을 기준으로 업데이트
    2-1. now_room의 첫번쨰 값이 대기 중인 시작 시간보다 늦으면 now_room에 끝나는 시간 넣기
    2-2. now_room의 첫번쨰 값이 대기 중인 시작 시간보다 늦지 않는 경우 now_room의 값을 하나뺴고 대기 중인 회의 넣기 


[경우]
0 40
15 30
5 10

0 40 
5 10
15 30

2-1. 
now_room  = [40]
40 5 비교
-> now_room = [10, 40]

2-2
now_room = [10, 40]
10 15 비교
-> now_room = [30, 40]
"""


import heapq

# 입력
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

# 정렬하기 
info.sort()

# 최소 회의실 개수 찾기
now_room = [info.pop(0)[1]] # 회의가 끝나는 시각을 저장
for i in info:
    if now_room[0] > i[0]: # 회의 끝나는 시각이 대기중인 회의 시각보다 늦으면
        heapq.heappush(now_room, i[1])
    else: # 회의 끝나는 시각 다음에 대기중인 회의를 진행가능한 경우
        heapq.heappop(now_room)
        heapq.heappush(now_room, i[1])

# 출력
print(len(now_room))