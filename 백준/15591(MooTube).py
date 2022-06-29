# 15591 MooTube

"""
소 1~N
소들이 좋아할 만한 새 동영상
연관 동영상 리스트
가까운지 측정하는 단위 USADO 최소

"""
from collections import deque

# 질문에 맞는 동영상의 갯수 찾는 함수
def find_video(v, k, usado, link, N):
    check = deque()
    check.append((v, float('inf'))) # 시작하는 노드, 최소 값
    visited = [0 for _ in range(N+1)]
    visited[v] = 1
    cnt = 0
    
    while check:
        now_v, min_u = check.popleft()
        for next_v in link[now_v]:
            if visited[next_v]:
                continue
            
            next_u = usado[now_v][next_v]
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
twin = [list(map(int, input().split())) for _ in range(N-1)]

# 연결 데이터 생성
usado = [[0 for _ in range(N+1)] for __ in range(N+1)]
link = {i:[] for i in range(1, N+1)}
for p,q,r in twin:
    usado[p][q] = r
    usado[q][p] = r
    link[p].append(q)
    link[q].append(p)

# v 동영상을 보는 K 이상의 추천 동영상 갯수 찾기
for _ in range(Q):
    k, v = map(int, input().split())
    # 출력
    print(find_video(v, k, usado, link, N))