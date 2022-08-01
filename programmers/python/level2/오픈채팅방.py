def solution(record):
    
    # record 기록 정리
    answer = [] # (동작, 아이디)
    name = {} # 아이디: 이름
    for i in record:
        m = i.split()
        if(m[0] == 'Enter'):
            answer.append(('Enter', m[1]))
            name[m[1]] = m[2]
        elif(m[0] == 'Leave'):
            answer.append(('Leave', m[1]))
        elif(m[0] == 'Change'):
            name[m[1]] = m[2]
    
    # 메세지문 정리
    result = []
    for i in answer:
        if(i[0] == 'Enter'):
            result.append('{}님이 들어왔습니다.'.format(name[i[1]]))
        elif(i[0] == 'Leave'):
            result.append('{}님이 나갔습니다.'.format(name[i[1]]))
    return result