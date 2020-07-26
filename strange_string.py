def solution(s):
    answer = ''
    count = 0
    for w in s:
        if(count%2==0 and w.isalpha()):
            count+=1
            answer += w.upper()
        else:
            count+=1
            answer += w
            if(w == ' '):
                count = 0
    return answer

print(solution("try hello world"))