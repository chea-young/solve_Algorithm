def solution(heights):
    answer = []
    num = heights[-1]
    for i in range(len(heights)-2,-1, -1):
        now = heights[i]
        print(num, '------------------')
        if(now > num):
            print(now, num)
            answer.append(i+1)
        else:
            print('+++++++++++++++++++++++++++++++++')
            check = True
            for j in range(i-1,-1,-1):
                print(heights[j], num)
                if(heights[j]>num):
                    answer.append(j+1)
                    check = False
                    break
            if(check):
                answer.append(0)
        num = heights[i]
    answer.append(0)
    return list(reversed(answer))

#print(solution([6,9,5,7,4]))
print(solution([1,5,3,6,7,6,5]))