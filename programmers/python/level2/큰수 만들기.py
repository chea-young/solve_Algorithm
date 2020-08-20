def solution(number, k):
    answer_num = len(number)-k
    answer = []
    num = [i for i in number]
    max_num = num.index(max(num[:k]))
    k -= max_num
    check = num[max_num]
    answer.append(check)
    del num[:max_num+1]
    plus = k-1
    c = True
    for i in range (k):
        if(check != num[i]):
            c = False
            plus = i
            break
    if(plus !=0):
        answer += num[:plus]
        del num[:plus]
        if(len(answer) >= answer_num):
            ans = ''
            for i in answer[:answer_num]:
                ans += i
            return ans
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
print(solution("999999999999999999", 10))