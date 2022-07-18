# 1922 네트워크연결

""" 


"""
# x에 대한 루트 edge를 찾는 함수
def find_root(x, root):
    if root[x] != x:
        root[x] = find_root(root[x], root)
    return root[x]

# 입력
N = int(input())
M = int(input())
weight = []
for _ in range(M):
    s, e, v = map(int, input().split())
    weight.append([v, s, e])

# 최소 비용을 기준으로 정렬하기
weight.sort()

# 최소 비용 찾기
result = 0
root = [i for i in range(N+1)]
for v, s, e in weight:
    s_root = find_root(s, root)
    e_root = find_root(e, root)

    if s_root != e_root: # 서로 연결되어 있지 않는 경우
        result += v
        # 연결하기
        if s_root < e_root:
            root[e_root] = s_root
        else:
            root[s_root] = e_root

# 출력
print(result)