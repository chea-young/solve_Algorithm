import heapq

def solution(scoville, K):
    heap_s = []
    for i in range(len(scoville)):
        heapq.heappush(heap_s, scoville[i])
    print(heap_s)
    answer  = 0
    while(True):
        if(heap_s[0] >= K):
            break
        answer+=1
        try:
            heapq.heappush(heap_s,heapq.heappop(heap_s)+(heapq.heappop(heap_s)*2))
        except:
            return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))
print(solution([1, 2, 0, 0, 10, 12],7))
print(solution([1, 0, 0, 0, 10, 12],7))