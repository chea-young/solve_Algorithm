def solution(numbers):
    answer = sorted([str(i) for i in numbers], key=lambda x:(x[0],int(x)), reverse=True)
    last = answer[0]
    check = True
    while(check):
        check = False
        for i in range(len(answer)):
            now = answer[i]
            if(answer[i] == answer[0]):
                continue
            if(len(last)> len(now) and last[:len(now)] == now):
                if(int(now)>int(last[len(now):])):
                    check = True
                    answer[i] = last
                    answer[i-1] = now
            last = now
    num = ''
    for i in answer:
        num +=i
    return num

#print(solution([6,10,2]))
#print(solution([3, 30, 34, 5, 9,31]))
print(solution([1,112]))