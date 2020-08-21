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
    move_r = 0
    for i in range(1, len(word)):
        move_r +=1
        if(word[i] in f):
            num += f.index(word[i])
        else:
            num += b.index(word[i])
        if(word[i] == 'A'):
            check_a += 1
            move_r -=1
            check = True
        if(check and word[i] != 'A'):
            check = False
            move_r += check_a
            check_a = 0
    count.append(num+move_r)
    check_a = 0
    check = False
    num = start
    move_l = 0
    for i in range(len(word)-1, 0, -1):
        move_l +=1
        if(word[i] in f):
            num += f.index(word[i])
        else:
            num += b.index(word[i])
        if(word[i] == 'A'):
            check_a += 1
            move_l -=1
            check = True
        if(check and word[i] != 'A'):
            check = False
            move_l += check_a
            check_a = 0
    count.append(num+move_l)
    if(move_r == move_l):
        return count[0] -1
    return min(count)-1

print(solution("JEROEN")) #56
print(solution("JAN")) #23
print(solution("JANN")) #37
print(solution("JNAN")) # 38
print(solution("BBBAAAB"))#10
