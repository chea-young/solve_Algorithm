# 02075 N번째 큰수

# 자신의 위에 있는 수봐 큼

import heapq
import sys

#입력
N = int(input())

check_list = [] # N의 개수를 유지하는 리스트
for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    
    if not check_list:
        for ele in data:
            heapq.heappush(check_list, ele)
    else:
        for ele in data:
            if ele > check_list[0]:
                heapq.heappop(check_list)
                heapq.heappush(check_list, ele)
#출력
print(check_list[0])
