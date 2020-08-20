def solution(number, k):
    answer_num = len(number)-k
    answer = []
    num = [i for i in number]
    max_num = 0
    while(k!=0):
        max_n = max(num[:k+1])
        if(max_n == min(num[:k+1])):
            num = num[k:]
            break
        max_num = num.index(max_n)
        answer.append(num[max_num])
        del num[:max_num+1]
        k -= max_num
    num = answer + num
    answer = ''
    for i in num:
        answer += i
    return answer

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("111211111",4))