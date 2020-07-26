def solution1(dartResult):
    answer = [0]*3
    count_idex =[]
    s_list = []
    n = ''
    for i in range(len(dartResult)):
        if(dartResult[i].isdigit()):
            n +=dartResult[i]
        else :
            if(n != ''):
                count_idex.append(i-len(n))
                s_list.append(int(n))
                n = ''
    score = [
        dartResult[:count_idex[1]], 
        dartResult[count_idex[1]:count_idex[2]], 
        dartResult[count_idex[2]:]
        ]
    option = ['S','D','T']
    extra = []
    for i in score:
        bonus = list(set(option) & set(i))
        if('*' in i):
            extra.append([bonus[0],'*'])
        elif('#' in i):
            extra.append([bonus[0],'#'])
        else:
            extra.append([bonus[0],0])
    for i in range(3):
        num = (s_list[i])**(option.index(extra[i][0])+1)
        if(extra[i][1] == '*'):
            if(i==0):
                answer[i] = (num*2)
                continue 
            answer[i-1] *= 2
            answer[i] = (num*2)
        elif(extra[i][1]=='#'):
            answer[i] = (num*(-1)) 
        else:
            answer[i] = num
    return sum(answer)

def solution(dartResult):
    answer = []
    n = ''
    option = ['S','D','T']
    count = 0
    for i in dartResult:
        if( i.isdigit() ):
            n += i
            count+=1
        elif(i.isalpha()):
            answer.append(int(n)**(option.index(i)+1))
            n = ''
        else:
            if(i == '*'):
                if(count ==1):
                    answer[count-1] *=2
                    continue
                answer[count-1] *=2
                answer[count-2] *=2
            elif(i == '#'):
               answer[count-1] *= (-1)
    return sum(answer)


print(solution('1D2S#10S'), '9')
print(solution('1D2S0T'), '3')
print(solution('1S2D*3T'), '37')
print(solution('1S*2T*3S'), '23')
print(solution('1D#2S*3S'), '5')
print(solution('1T2D3D#'), '-4')
print(solution('1D2S3T*'), '59')
