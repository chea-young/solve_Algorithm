import heapq
import sys
 
#입력
N, K = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]
 
# 정렬
jewels.sort()
bags.sort()
 
# 가방의 무게보다 작거나 같은 보석에서 최대 가치인 보석 찾기
answer = 0
data = []
for b in bags:
    while jewels and b >= jewels[0][0]:
        heapq.heappush(data, (-1)*jewels[0][1])
        heapq.heappop(jewels)
                
    if data: # 가방에 넣을 수 있는 보석이 있는 경우
        answer += (-1) * heapq.heappop(data)
        
# 출력
print(answer)
