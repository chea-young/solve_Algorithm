# 덩치
num = int(input())
# 입력
data= []
for i in range(num): #입력
    ele = [int(i) for i in input().split()]
    data.append((ele[0], ele[1]))

for standard in data:
    order = 1
    for compare in data: # 등수 계산
        if standard == compare: continue
        if standard[0] < compare[0] and standard[1] < compare[1]:
            order +=1
    print(order) # 출력
