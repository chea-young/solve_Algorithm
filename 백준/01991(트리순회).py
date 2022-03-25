# 1991 트리 순회

#입력
N = int(input())
data = {}
for _ in range(N):
    root, left, right = map(str, input().split())
    data[root] = (left,right)

def preorder(check): #queue
    if check != '.':
        print(check, end='')
        preorder(data[check][0])
        preorder(data[check][1])
    
 
def midorder(check):
    if check != '.':
        midorder(data[check][0])
        print(check, end='')
        midorder(data[check][1])
    
def lastorder(check):
    if check != '.':
        lastorder(data[check][0])
        lastorder(data[check][1])
        print(check, end='')

preorder('A')
print()
midorder('A')
print()
lastorder('A')
