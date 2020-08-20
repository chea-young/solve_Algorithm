def solution(number, k):
    answer = []
    num = [i for i in number]
    max_num = num.index(max(num[:k]))
    answer.append(num[max_num])
    del num[:max_num+1]
    k -= max_num
    # 통과
    while(k!=0):
        try:
            max_num = num.index(max(num[:k+1]))
        except ValueError:
            num = answer + num
            max_num = num.index(max(num[:k+1]))
        if(k<max_num):
            index = max_num
            continue
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