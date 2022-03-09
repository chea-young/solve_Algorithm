# 2110 공유기 설치

# 입력
N, C = map(int, input().split())
data = [int(input()) for i in range(N)]
f, end = min(data), max(data)

installed = [0] * (end+1)
installed[f] = 1
installed[end] = 1
in_list = [f, end]

def find_dis(num): # 가장 인접한 공유기 사이 구하는 함수
    dis_list = []
    for ele in in_list:
        dis_list.append(abs(ele-num))
    return min(dis_list)

for count in range(C-2):
    dis = 0
    check_i = 0
    for i, ele in enumerate(data):
        if installed[ele] == 1:
            continue
        dis_i = find_dis(ele)
        if dis_i > dis:
            dis = dis_i
            check_i = ele
    installed[check_i] = 1
    in_list.append(check_i)
    
# 출력
answer = end-f
for i in in_list:
    for j in in_list:
        if i != j:
            answer = min(answer, abs(i-j))
print(answer)
