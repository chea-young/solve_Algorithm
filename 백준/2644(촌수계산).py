# 촌수계산 2644
# 부모 - 자식 1촌, 형제 +2촌

class Node:
    def __init__(self, id, parent=False, child=[]):
        self.parent = parent
        self.child = child
        self.id = id
        
    def __str__(self):
        return self.id
    
    def check(self):
        print(f'--{self.id}--{self.parent}---{self.child}')

def find(parent, child):
    answer = 0
    visited = [0] * (n+1)
    print(f'{answer}, check: node: {child}')
    now_p = rel[child].parent
    visited[child] = 1
    while now_p != parent: # parent 찾기
        answer +=1
        print(f'{answer}, check: node: {now_p}')
        if rel[now_p].parent == False:
            break
        now_p = rel[now_p].parent
        visited[now_p] = 1
        
    now_c = rel[now_p].child # child 찾기
    print(f'{answer}, check: node: {now_p} {now_c}')
    while True:
        answer += 1
        print(f'{answer}, check: node: {now_p} {now_c}')
        if parent in now_c:
            break
        if now_c == []:
            answer = -1
            break
        ele = []
        for i in now_c:
            if visited[i] == 0:
                visited[i] = 1
                ele += rel[i].child
        now_c = ele
    return answer
        
# 입력
n = int(input())
p1, p2 = map(int, input().split())
rel = [0] * (n+1)
for i in range(int(input())):
    x, y = map(int, input().split()) #x 부모, y 자식
    if rel[x] == 0:
        rel[x] = Node(x, child = [y])
    else: 
        rel[x].child.append(y)
    if rel[y] == 0:
        rel[y] = Node(y, parent = x, child = [])
    else:
        rel[y].parent = x

# 촌수찾기
answer = find(p1, p2)

#출력
print(answer)
