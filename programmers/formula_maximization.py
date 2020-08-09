def solution(expression):
    answer = []
    num_list = []
    opr_list = []
    opr_2 = [(0,1), (1,0)]
    opr_3 = [(0,1,2), (0,2,1), (1,0,2), (1,2,0),(2,0,1), (2,1,0)]
    num = ''
    for i in expression:
        if(i in '0123456789'):
            num += i
        else:
            num_list.append(int(num))
            num = ''
            num_list.append(i)
            opr_list.append(i)
    num_list.append(int(num))
    opr_list = list(set(opr_list))
    if(len(opr_list) == 2):
        for i in range(2):
            num = num_list[:]
            num = cal(num, opr_list[opr_2[i][0]])
            num = cal(num, opr_list[opr_2[i][1]])
            answer.append(abs(num[0]))
    elif(len(opr_list) == 3):
        for i in range(6):
            num = num_list[:]
            num = cal(num, opr_list[opr_3[i][0]])
            num = cal(num, opr_list[opr_3[i][1]])
            num = cal(num, opr_list[opr_3[i][2]])
            answer.append(abs(num[0]))
    else:
        num = num_list[:]
        num = cal(num, opr_list[0])
        answer.append(abs(num[0]))
    return max(answer)

def cal(num_list, opr):
    while(True):
        try:
            index = num_list.index(opr)
        except ValueError:
            break
        if(opr =='*'):
            num1 = num_list[index+1]
            num2 = num_list[index-1]
            num_list[index-1] = num1*num2
            del num_list[index+1]
            num_list.remove('*') 
        elif(opr == '-'):
            num1 = num_list[index+1]
            num2 = num_list[index-1]
            num_list[index-1] = num2-num1
            del num_list[index+1]
            num_list.remove('-') 
        elif(opr == '+'):
            num1 = num_list[index+1]
            num2 = num_list[index-1]
            num_list[index-1] = num1+num2
            del num_list[index+1]
            num_list.remove('+') 
    return num_list

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(solution("50-60-10"))