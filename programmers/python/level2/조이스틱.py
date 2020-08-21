def solution(name):
    f = 'ABCDEFGHIJKLM'
    b = 'AZYXWVUTSRQPON'
    word = [i for i in name]
    count = []
    def count_num(start, end, n):
        move = 0
        num = 0
        check_a = 0
        check = False
        if(word[0] in f):
            num = f.index(word[0])+1
        else:
            num = b.index(word[0])+1
        for i in range(start, end, n):
            move +=1
            if(word[i] in f):
                num += f.index(word[i])
            else:
                num += b.index(word[i])
            if(word[i] == 'A'):
                check_a += 1
                move -=1
                check = True
            if(check and word[i] != 'A'):
                check = False
                move += check_a
                check_a = 0
        return (move, num)
    num_a = []
    a = 0
    check = False
    start = 0
    for i in range(len(word)):
        if(word[i] == 'A'):
            a+=1
            check = True
            start = i
        else:
            check = False
            if(a>=2):
                num_a.append((a,start,i))
            a=0
    num_a = sorted(num_a,key=lambda x: x[0], reverse = True)
    check = False
    if(len(word[:num_a[0][1]])<num_a[0][0] and len(word[num_a[0][2]+1:])<num_a[0][0]):
        check = True
    if(len(word[:num_a[0][1]])<len(word[num_a[0][2]+1:])):
        num = len(word[:num_a[0][1]])+count_num(num_a[0][1]-1, -1,-1)+1+count_num(len(word)-1,num_a[0][2],-1)
    else:
        pass



    move_r, num = count_num(1,len(word),1)
    count.append(num+move_r)
    move_l, num = count_num(len(word)-1,0,-1)
    count.append(num+move_l)
    if(move_r == move_l):
        return count[0] -1
    return min(count)-1



print(solution("JEROEN")) #56
print(solution("JAN")) #23
print(solution("JANN")) #37
print(solution("JNAN")) # 38
print(solution("BBBAAAB"))#10
print(solution("ABABAAAAABA")) #11
