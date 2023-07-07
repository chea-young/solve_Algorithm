# 19640 화장실의 규칙

"""
[우선순위]
1. 근무일이 많은 경우
2. 급한 정도가 높은 경우
3. 줄 번호가 작은 경우
"""
import sys
import heapq
from collections import deque

def input_data():
    input_func = sys.stdin.readline
    N, M, K = map(int, input_func().split())
    line_list = [deque() for _ in range(M)] # 근무일, 급한정도, 줄번호, 자신의 원래 순서
    check_list = [0] * M # 해당 줄에 사원이 남아있는지 확인하는 리스트
    for i in range(N):
        line_num = i%M
        work_day, hurry_num = map(int, input_func().split())
        line_list[line_num].append([(-1)*work_day, (-1)*hurry_num, line_num, i])
        check_list[line_num] += 1
    return N, M, K, line_list, check_list

def solve(N, M, K, line_list, check_list):
    # put worker in each line
    heapq_list = []
    for i in range(M):
        if check_list[i] == 0:
            continue

        heapq.heappush(heapq_list, line_list[i].popleft())
        check_list[i] -= 1
    
    # check worker's order
    answer = 0
    while True:
        work_day, hurry_num, line_num, original_line_num = heapq.heappop(heapq_list)
        
        if original_line_num == K: ## find worker
            return answer
        
        answer += 1
        if check_list[line_num] > 0: ## if the worker exists in the line
            heapq.heappush(heapq_list, line_list[line_num].popleft())
            check_list[line_num] -= 1
    return answer
    
# 입력
N, M, K, line_list, check_list = input_data()

# 출력
print(solve(N, M, K, line_list, check_list))