# 20040 사이클 게임

# 선 -> 홀 / 후 -> 짝
# 일직선 X
# 두 점을 선택에 연결 - 다시 X, 교차 0

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    
    if x == y: # 사이클이 만들어졌을 경우
        return True
    elif x < y:
        parent[y] = x
    else:
        parent[x] = y
    return False

#입력
dotNum, progressNum = map(int, input().split())
data = [map(int, input().split()) for _ in range(progressNum)]
        
parent = [i for i  in range(0, dotNum+1)]
for i, [dot1, dot2] in enumerate(data):
    check = union(dot1, dot2, parent)
    if check:
        print(i+1)
        break
else:
    print(0)
