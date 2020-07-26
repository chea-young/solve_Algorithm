def solution(expression):
    num_list = []
    opr_list = []
    num = ''
    for i in expression:
        if(i in '0123456789'):
            num += i
        else:
            num_list.append(int(num))
            num = ''
            num_list.append(i)
    num_list.append(int(num))
    opr1 = True
    opr2 = True
    opr3 = True
    while(len(num_list) != 1):
        try:
            if(opr1):
                index = num_list.index('*')
        except ValueError:
            opr1 = False
        if(opr1):
            num1 = num_list[index+1]
            num2 = num_list[index-1]
            num_list[index-1] = num1*num2
            del num_list[index+1]
            num_list.remove('*')
            continue
        try:
            if(opr2):
                index = num_list.index('+')
        except ValueError:
            opr2 = False
        if(opr2):
            num1 = num_list[index+1]
            num2 = num_list[index-1]
            num_list[index-1] = num1+num2
            del num_list[index+1]
            num_list.remove('+')
            continue
        try:
            if(opr3):
                index = num_list.index('-')
        except ValueError:
            opr3 = False
        if(opr3):
            num1 = num_list[index+1]
            num2 = num_list[index-1]
            num_list[index-1] = num2-num1
            del num_list[index+1]
            num_list.remove('-')
            continue
    return abs(num_list[0])

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))