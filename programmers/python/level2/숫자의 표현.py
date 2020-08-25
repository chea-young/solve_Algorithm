def solution(n):
    answer = 0
    for num in range(1,n+1):
        check =0
        for i in range(num,n+1):
            check += i
            if(check>n):
                break
            elif(check == n):
                answer +=1
                break
    return answer