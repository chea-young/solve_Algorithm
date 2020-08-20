def solution(number, k):
    num = [i for i in number]
    max_num = num.index(max(num[:k]))
    answer = num[max_num]
    num = num[max_num+1:]
    k -= max_num
    index = len(num)
    while(k!=0):
        max_num = num.index(max(num[:index]))
        if(k<max_num):
            index = max_num
            continue
        answer += num[max_num]
        num = num[max_num+1:]
        k -= max_num
        index = len(num)
    for i in num:
        answer += i
    return answer

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))