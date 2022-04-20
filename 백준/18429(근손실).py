# 18429 근손실
from itertools import permutations

# 입력
N, K = map(int, input().split())
increase = list(map(int, input().split()))
case = permutations(increase, N) # 모든 경우의 수 구하기
answer = 0
for ele in case:
    check = 0
    for weight in ele:
        check -= K
        check += weight
        if check < 0:
            break
    else: # 경우를 만족하는 경우
        answer += 1
    
# 출력
print(answer)
