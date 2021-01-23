def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i==j :
                continue
            answer.append(numbers[i]+numbers[j])
    answer = set(answer)
    return sorted(list(answer))