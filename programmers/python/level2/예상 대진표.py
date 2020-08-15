def solution(n,a,b):
    arr = []
    num = 1
    while(num<=n):
        one = num
        two = num+1
        num +=2
        if(one== a and two == b):
            return 1
        elif(two == a and one == a):
            return 1
        elif(one== a or two == a):
            arr.append(a)
        elif(one== b or two == b):
            arr.append(b)
        else:
            arr.append(one)
            
    answer =1
    while(True):
        temp = []
        number = 0
        while(number<len(arr)):
            one = arr[number]
            if(number+1 == len(arr)):
                temp.append(one)
                break
            two = arr[number+1]
            number +=2
            if(one== a and two == b):
                return answer +1
            elif(two == a and one == a):
                return answer +1
            elif(one== a or two == a):
                temp.append(a)
            elif(one== b or two == b):
                temp.append(b)
            else:
                temp.append(one)
        arr=temp
        answer +=1

print(solution(7,4,7))
print(solution(10,4,7))