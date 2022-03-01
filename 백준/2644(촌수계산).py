# 촌수계산 2644
# 부모 - 자식 1촌, 형제 +2촌

class Node:
    def __init__(self, id, parent=False, child=False):
        self.parent = parent
        self.child = child
        self.id = id
        
    def __str__(self):
        return self.id
    
    def check(self):
        print(f'--{self.id}--{self.parent}---{self.child}')

def find(parent, child):
    answer = 0
    now_p = rel[child].parent
    while now_p != parent:
        if now_p == False:
            answer = -1 # 친척 관계가 없을 때
            break
        answer +=1
        now_p = rel[now_p].parent
        if now_p and parent in rel[now_p].child:
            answer += 2
            break
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
answer1 = find(p1, p2)
answer2 = find(p2, p1)

#출력
if answer1 == answer2 == -1:
    print(-1)
elif answer1 == -1:
    print(answer2)
elif answer2 == -1:
    print(answer1) 
