def solution(numbers):
    max_num = len(str(max(numbers)))
    num = [str(i) for i in numbers]
    num_order = []
    for i in range(len(num)):
        num_order.append((num[i], num[i]+num[i][-1]*(max_num-len(num[i]))))
    answer = sorted(num_order, key=lambda x:x[1], reverse=True)
    print(answer)
    n = ''
    for i in range(len(answer)):
        n += answer[i][0]
    return str(int(n))

#print(solution([6,10,2]))
#print(solution([3, 30, 34, 5, 9]))
#print(solution([0,0,0,0,0]))
print(solution([242,424,242]))
print(solution([1,2,22,3,4,5,6,7,8]))
#print(solution([21, 212]))
#print(solution([21, 212]))

