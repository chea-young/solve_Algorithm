def solution(participant, completion):
    p_dict = {}
    c_dict = {}
    for ele in participant:
        if ele in p_dict.keys():
            p_dict[ele] = p_dict[ele] + 1
        else:
            p_dict[ele] = 1
            
    for ele in completion:
        if ele in c_dict.keys():
            c_dict[ele] = c_dict[ele] + 1
        else:
            c_dict[ele] = 1

    for ele in participant:
        try:
            if c_dict[ele] != p_dict[ele]:
                return ele
        except KeyError:
            return ele
        
def solution(participant, completion):
    # 리스트 정렬
    participant.sort()
    completion.sort()
    # 완주하지 못한 선수 찾기
    while completion:
        eleP = participant.pop()
        eleC = completion.pop()
        # 완주한 선수 이름과 참가 이름이 같지 않은 경우 -> 완주 못한 선수 반환
        if eleP != eleC:
            return eleP
    
    return participant.pop()
