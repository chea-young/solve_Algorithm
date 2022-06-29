# 15591 MooTube
from collections import defaultdict, deque

# 질문에 맞는 동영상의 갯수 찾는 함수
def find_video(v, k, link, N):
    check = deque()
    check.append((v, float('inf'))) # 시작하는 노드, 최소 값
    visited = [-1] * N
    visited[v] = 1
    cnt = 0
    
    while check:
        now_v, min_u = check.popleft()
        for next_v, next_u in link[now_v]:
            if visited[next_v] == 1:
                continue
            
            if min_u > next_u:
                check.append((next_v, next_u))
                if next_v >= k:
                    cnt += 1
            else:
                check.append((next_v, min_u))
                if min_u >= k:
                    cnt += 1    
            visited[next_v] = 1
    return cnt

# 입력
N, Q = map(int, input().split())

# 연결 데이터 생성
link = defaultdict(list)
for _ in range(N-1):
    p, q, r = map(int, input().split())
    link[p-1].append((q-1, r))
    link[q-1].append((p-1, r))

# v 동영상을 보는 K 이상의 추천 동영상 갯수 찾기
for _ in range(Q):
    k, v = map(int, input().split())
    # 출력
    print(find_video(v-1, k, link, N))