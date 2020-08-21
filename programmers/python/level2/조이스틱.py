"""def solution(name):
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
"""
def solution(name):
    f = 'ABCDEFGHIJKLM'
    b = 'AZYXWVUTSRQPON'
    word = [i for i in name]
    count = []
    num = 0
    if(word[0] in f):
        num = f.index(word[0])+1
    else:
        num = b.index(word[0])+1
    start = num
    check_a = 0
    check = False
    for i in range(1, len(word)):
        if(word[i] in f):
            num += f.index(word[i])+1
        else:
            num += b.index(word[i])+1
        if(word[i] == 'A'):
            check_a += 1
            num-=1
            check = True
        if(check and word[i] != 'A'):
            check = False
            num+=check_a
            check_a = 0
    count.append(num)
    check_a = 0
    check = False
    num = start
    for i in range(len(word)-1, 0, -1):
        #print('check',num)
        if(word[i] in f):
            num += f.index(word[i])+1
        else:
            num += b.index(word[i])+1
        if(word[i] == 'A'):
            check_a += 1
            num-=1
            check = True
        if(check and word[i] != 'A'):
            check = False
            num+=check_a
            check_a = 0
    count.append(num)
    return min(count)-1

print(solution("JEROEN")) #56
print(solution("JAN")) #23
print(solution("JANN"))
print(solution("JNAN"))
print(solution("BBBAAAB"))
