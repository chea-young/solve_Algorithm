import sys

"""
k개를 골라 담아 판매 
-> 다른 종류의 수를 최소화

"""

def solution(k, tangerine):
    # 초기 세팅
    t_type = {}
    for t in tangerine:
        t_type[t] = t_type.get(t, 0) + 1
    t_type_cnt = sorted(list(t_type.items()), key=lambda x:x[1], reverse=True)
    
    # 최소 종류 갯수 구하기
    cnt = 0
    answer = 0
    for ts, tc in t_type_cnt:
        if cnt < k:
            answer += 1
            cnt += tc
    return answer

# 출력
print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]) == 3)
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]) == 2)
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]) == 1)
