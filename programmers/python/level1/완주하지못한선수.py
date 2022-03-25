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
    
            
