# 빗물 14719

# 위에서 아래로 검사
# if 검->흰 일 때 다음 검은 색 까지 추가
# 1 1 1 0
# 0 0 0 0
# 1 0 0 0
# 1 1 1 1

#입력
H, W = map(int, input().split())
data = list(map(int, input().split()))
max_num = max(data)

# 빗물 블럭 만들기
block = [] 
for i in range(len(data)):
    block.append([1]*data[i] + [0]*(max_num-data[i]))

# 빗물 찾기
answer = 0
for i in range(max_num):
    pre = 0
    check_in = False # 빗물 안의 부분인지
    ele = 0
    for j in range(len(data)):
        if pre == 1 and block[j][i] == 0: # 1 0 
            check_in = True
            ele += 1
        elif check_in and block[j][i] == 1: # 0 1
            check_in = False
            answer += ele
            ele = 0
        elif check_in: # 0 0
            ele += 1
        elif block[j][i] == 1:
            pre = 1
print(answer) #출력
