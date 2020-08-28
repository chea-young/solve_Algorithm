def solution(name):
    answer = 0
    index = 0
    f = 'ABCDEFGHIJKLM'
    b = 'AZYXWVUTSRQPON'
    word = [i for i in name]
    while(True):
        right = 0
        left = 0
        if(word[index] in f):
            answer += f.find(word[index])
        else:
            answer += b.find(word[index])
        word[index] = 'A'
        if(word == ['A']*len(word)):
            break
        for i in range(len(word)):
            if(right ==0 and word[i] != 'A'):
                right = i
            if(word[i] != 'A'):
                left = i
        left_check = index-left
        if(left_check<0):
            left_check = len(word)-left+index
        if(abs(right-index)<=left_check):
            answer += abs(right-index)
            index = right
        else:
            answer += left_check
            index = left
    return answer

print(solution("JEROEN")) #56
print(solution("JAN")) #23
print(solution("JANN")) #37
print(solution("JNAN")) # 38
print(solution("BBBAAAB"))#9
print(solution("ABABAAAAABA")) #11
        
