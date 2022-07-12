# 19598 최소 회의실 개수

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