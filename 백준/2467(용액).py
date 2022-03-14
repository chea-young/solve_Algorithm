# 2467 용액

# 산성 -> 양수, 알칼리성 -> 음수
# 0에 가장 가까운 값 만들기

# 입력
N = int(input())
liquid = list(map(int, input().split()))

l1_i = 0
l2_i = N-1
while True:
    mix = liquid[l1_i]+liquid[l2_i]
    if mix == 0: # 0에 가장 가까운 용액인 경우
        break
    elif mix > 0: # dif: 양수 -> l2가 왼쪽
        now_dif = liquid[l1_i]+liquid[l2_i-1]
        if abs(now_dif) <= abs(mix): # 변경 된 값이 0에 더 가까울 때
            l2_i -= 1
        else: break
    elif mix < 0:# dif: 음수 -> l1이 오른쪽
        now_dif = liquid[l1_i+1]+liquid[l2_i]
        if abs(now_dif) <= abs(mix):
            l1_i += 1
        else: break
            
    if l2_i >= l1_i:# l2가 l1보다 앞에 있거나 같으면 out
        break
#출력
print(liquid[l1_i], liquid[l2_i])
