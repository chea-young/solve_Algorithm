# 2529 부등호
from itertools import permutations

# 입력
k = int(input())
data = input().split()

def findPossible(case, data):
    for i, ele in enumerate(data):
        firstNum = int(case[i])
        secondNum = int(case[i+1])
        if ele == '<' and not (firstNum < secondNum):
            return False
        elif ele == '>' and not (firstNum > secondNum):
            return False
    return True
    
# 모든 경우의 수 찾기
allCase = permutations([str(i) for i in range(10)], k+1)
answer = []
for ele in allCase:
    check = findPossible(ele,data)
    if check:
        answer.append(ele)

# 출력
print(''.join(max(answer)))
print(''.join(min(answer)))
