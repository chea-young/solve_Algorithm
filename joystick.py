def solution(name):
    f = 'ABCDEFGHIJKLM'
    b = 'AZYXWVUTSRQPON'
    word = [i for i in name]
    location = True
    index = 0
    answer = 0
    while(True):
        next = ''
        if(location == False ):
            next = word[index-1]
        elif(location and index != len(word)-1):
            next = word[index +1]
        if(word[index] in f):
            answer += f.index(word[index])
        elif(word[index] in b):
            answer += b.index(word[index])
        if ((location == True and index == len(word)-1) or (location == False and index-1 == 0)):
            if(word[index] == 'A'):
                answer -=1
            break
        if(index == 0 and word[index+1] == 'A'):
            location = False
            index = len(word)-1
            answer += 1
        else:
            answer += 1
            if(location):
                index +=1
            else:
                index -=1
    return answer

#print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JANN"))
print(solution("JNAN"))
print(solution("BBBAAAB"))
