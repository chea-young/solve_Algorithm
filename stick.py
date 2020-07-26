def solution(arrangement):
    lasor = []
    stick = []
    stack = []
    for i in range(len(arrangement)):
        if(arrangement[i] == '('):
            stack.append((i,len(lasor)))
        else:
            item = stack.pop()
            if(i-item[0] == 1):
                lasor.append(i)
            else:
                stick.append(len(lasor)- item[1]+1)
    return sum(stick)

print(solution("()(((()())(())()))(())"))