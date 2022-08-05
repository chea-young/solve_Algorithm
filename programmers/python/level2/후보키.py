"""
후보키의 최대 개수
유일성 -> 최소성

1. 1- len(relation[1])만큼 for문 돌기
    1-1. 현재 찾는 키 기준이 now_key에 있는지 확인 있으면 continue로 넘기기
    2. now_key에 없는 경우 for문을 돌 때까지 중복되는 정보가 없으면 now_key에 튜플로 넣음
"""
from itertools import combinations

# 최소성 조건을 확인하는 함수
def check_minimality(now_key, key):
    for k in now_key:
        if set(key) & set(k) == set(k): # 최소성을 만족하지 못 하는 경우
            return False
    return True

# 유일성 조건을 확인하는 함수
def check_uniqueness(relation, key):
    check_list = []
    for r in relation:
        temp = []
        for k in key:
            temp.append(r[k])
        if temp in check_list:
            return False
        check_list.append(temp)
    return True

def solution(relation):
    now_key = set()
    column_cnt = len(relation[0])
    
    # 모든 케이스 다 찾기
    all_case = []
    temp = [i for i in range(column_cnt)]
    for i in range(1, column_cnt+1):
        all_case += list(combinations(temp, i))

    # 후보키 찾기
    for key in all_case:
        # 최소성 확인
        if not check_minimality(now_key, key):
            continue
        
        # 유일성 확인
        if not check_uniqueness(relation, key):
            continue
        
        # 두 가지 조건을 만족하는 경우
        now_key.add(key)

    return len(now_key)

relation1 = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# 반례
relation2 = [['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']] # 정답 3

print(solution(relation1))