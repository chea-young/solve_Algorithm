def solution(prices):
    answer = []
    count = 0
    for i in prices:
        count += 1
        sec = 0
        check = True
        for j in prices[count:]:
            sec += 1
            if(j<i):
                answer.append(sec)
                check = False
                break
        if(check):
            answer.append(sec)
    return answer

def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)):
        for j in prices[i+1:]:
            answer[i] +=1
            if(j<prices[i]):
                break
    return answer

print(solution([1,2,3,2,3]))