def solution(people, limit):
    people.sort()
    answer = 0
    start =0
    end = len(people)-1
    while(start<=end):
        if(start ==end):
            return answer +1
        if(people[start] + people[end] <= limit):
            answer +=1
            start +=1
            end -= 1
        else:
            answer +=1
            end -= 1
    return answer 

print(solution([70, 50, 80, 50],100))
print(solution([70, 80, 50],100))