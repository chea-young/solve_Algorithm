# 2467 용액

# 산성 -> 양수, 알칼리성 -> 음수
# 0에 가장 가까운 값 만들기

# 입력
N = int(input())
liquid = list(map(int, input().split()))

l1_i = 0
l2_i = N-1
answer = [0, N-1]
min_mix = abs(liquid[l1_i]+liquid[l2_i])

while l1_i < l2_i:
    mix = liquid[l1_i]+liquid[l2_i]
    if abs(mix) < abs(min_mix): # 현재 값이 더 0에 가까운 경우
        answer[0] = l1_i
        answer[1] = l2_i
        min_mix = abs(mix)
    
    if mix > 0: # dif: 양수 -> l2가 왼쪽
        l2_i -= 1
    elif mix < 0:# dif: 음수 -> l1이 오른쪽
        l1_i += 1
    else:
        break
#출력
print(liquid[answer[0]], liquid[answer[1]])
