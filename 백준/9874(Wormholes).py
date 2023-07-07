# 10021 Watering the Fields
import heapq
import sys

def cal_Euclidean(i, j):
    return abs(i[0]-j[0])**2 + abs(i[1]-j[1])**2

def find(node):
    if parents[node] == node: 
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
    
def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: # 이미 연결이 된 것이기 때문에
        return False
    else:
        parents[root2] = root1
        return True

# 입력
N, C = map(int, sys.stdin.readline().rstrip().split())
loc = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

parents = [i for i in range(N)]
data = [] # [비용, i, j] -> C 보다 큰 최소 비용을 연결하기 위해

# 유클리드 거리 업데이트하기
for i in range(N):
    for j in range(i+1, N):
        cost = cal_Euclidean(loc[i], loc[j])
        if cost >= C:
            heapq.heappush(data, [cost, i, j])

# 최소 파이프 연결하기
total = 0
edge_num = 0
while data:
    now_cost, node1, node2 = heapq.heappop(data)
    
    if union(node1, node2):
        total += now_cost
        edge_num += 1
        if edge_num == N-1: # 전체를 연결하는 최대 edge 수가 N-1 이기 때문에
            break

if edge_num == N-1:
    print(total)
else:
    print(-1)