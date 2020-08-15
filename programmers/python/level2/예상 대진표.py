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
    temp = []
    number = 0
    answer = 1
    while(True):
        one = arr[number]
        two = -1
        if(number+1 != len(arr)):
            two = arr[number+1]
            number +=2
        else:
            number +=1
        if(one== a and two == b):
            return answer +1
        elif(two ==-1):
            temp.append(one)
        elif(two == a and one == a):
            return answer +1
        elif(one== a or two == a):
            temp.append(a)
        elif(one== b or two == b):
            temp.append(b)
        else:
            temp.append(one)
        if(number == len(arr)):
            arr=temp
            answer+=1
            temp = []
            number = 0

print(solution(7,4,7))
print(solution(10,4,7))