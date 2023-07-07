# 1939 중량제한

"""
섬 -> 다리
섬에 공장을 세워 물품 생산
다리 중량제한
0
- 여러 개의 다리 존재, 양방향

"""
from collections import deque

# 입력
N, M = map(int, input().split())
conn = {} # 섬에 연결되어 있는 정보 {섬: [섬1, 섬2]} 1, 2,3 1-2
weight = [[set() for __ in range(N+1)] for _ in range(N+1)] # 가중치를 저장하는 리스트
for i in range(M):
    A, B, C = map(int, input().split())
    conn[A] = conn.get(A, []) + [B]
    conn[B] = conn.get(B, []) + [A] #default dict
    weight[A][B].add(C)
    weight[B][A].add(C)
start, end = map(int, input().split())

# 중량의 최댓값 구하기
answer = False
visited = [0] * (N+1)
check = deque() # [현재 위치, weight]
check.append([start, 0]) 
visited[start] = 1
while check:
    try:
        now_loc, now_weight = check.popleft()
        print(now_loc, now_weight)
    except:
        print("in")

    # 목적지에 도착했을 때
    if now_loc == end:
        if not answer or now_weight > answer:
            answer = now_weight
    
    # 연결되어 있는 섬에 확인
    for i in conn[now_loc]:
        for w in weight[now_loc][i]:
            if not visited[i]:
                if w > now_weight:
                    check.append([i, now_weight+w])
        visited[i] = 1

# 출력
print(answer)
