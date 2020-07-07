def solution(d, budget):
    answer = 0
    length = len(d)
    for i in range(length):
        num = min(d)
        answer+=num
        d.remove(num)
        if(answer>budget):
            return i
        elif(answer == budget):
            return i +1
    return length

d1 =[1,3,2,5,4]
d2 =  [2,2,3,3]

print(solution(d1, 9)) #3
print(solution(d2, 10)) #4