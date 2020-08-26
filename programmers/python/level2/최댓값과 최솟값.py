def solution(s):
    minus = ''
    num = ''
    answer = []
    for i in s:
        if(i == '-'):
            minus = '-'
        elif(i.isdigit()):
            num +=i
        else:
            if(minus == '-'):
                answer.append(int(num)*(-1))
            else:
                answer.append(int(num))
            minus = ''
            num = ''
    if(minus == '-'):
        answer.append(int(num)*(-1))
    else:
        answer.append(int(num))    
    answer.sort()
    return str(answer[0])+" "+str(answer[-1])

print(solution("1 2 3 4"))
print(solution("4 -2 3 -5"))
print(solution("4 -2 10 -5"))