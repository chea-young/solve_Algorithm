# 01043 거짓말
import sys

"""
사람 수: N
party_info = 사람 수, 오는 사람의 번호..

1. 진실을 아는 사람들이 가는 파티 확인
2. 해당 파티에서 진실을 모르는 사람들이 누구인지 확인
3. 해당 사람들이 참석하는 파티들 제외
"""

def input_data(): # 입력받은 list에서 사람의 수는 지움
    input_func = sys.stdin.readline
    N, M = map(int, input_func().split())
    
    known_people_info = list(input_func().split())
    if len(known_people_info) > 1:
        known_people_info = known_people_info[1:]
    
    party_info = [set(list(input_func().split())[1:]) for _ in range(M)]
    return N, M, set(known_people_info), party_info

def solve(N, M, known_people_info, party_info):
    # init
    global checked
    
    checked = [1] * M # 0: can't go
    
    # 진실을 아는 사람이 없어 모든 파티에 참석 가능
    if known_people_info == set("0"):
        return M
    
    find_max_party(0)
    
    return sum(checked)

def find_max_party(party_i):
    # init
    global checked
    
    if party_i >= M or sum(checked) == 0:
        return
   
    if (checked[party_i]):
        intersection_set = known_people_info.intersection(party_info[party_i]) # 교집합
        difference_set = party_info[party_i].difference(known_people_info) # 차집합
        
        if (intersection_set): # 진실을 아는 사람이 존재하는 것
            checked[party_i] = 0 # 참석하지 못 하는 파티로 변경
            known_people_info.union(difference_set) # 진실을 몰랐던 사람도 아는 사람으로 변경
            find_max_party(0)
            
    find_max_party(party_i+1)


# 입력
N, M, known_people_info, party_info = input_data()

# 출력
print(solve(N, M, known_people_info, party_info))
