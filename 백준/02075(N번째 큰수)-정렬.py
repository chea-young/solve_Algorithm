# 02075 N번째 큰수

# 자신의 위에 있는 수봐 큼

import sys

#입력
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

def find_max(ele_list):
    max_num = 0
    in_max_num = 0
    for i, ele in enumerate(ele_list):
        if ele > max_num:
            max_num = ele
            in_max_num = i
    return max_num, in_max_num
    

check_line = [N-1 for _ in range(N)] # 현재 탐색할 라인 수
max_num = 0
cnt = N
while cnt != 0:
    next_max, in_next = find_max(data[N-1])
    max_num = next_max
    line = check_line[in_next]
    data[line][in_next] = 0
    if line != 0:
        check_line[in_next] = line-1
        data[N-1][in_next] = data[line-1][in_next]
    else:
        data[N-1][in_next] = 0
    cnt -= 1

#출력
print(max_num)
