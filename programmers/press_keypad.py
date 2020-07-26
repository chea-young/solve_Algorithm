def solution(numbers, hand):
    answer = ''
    left = -1
    right = -2
    for num in numbers:
        if(num in [1,4,7]):
            left = num
            answer += 'L'
        elif (num in [3,6,9]):
            right = num
            answer += 'R'
        else:
            n_dis = find_index(num)
            l_dis = find_index(left)
            r_dis = find_index(right)
            l = abs(l_dis[0]-n_dis[0]) + abs(l_dis[1]-n_dis[1])
            r = abs(r_dis[0]-n_dis[0]) + abs(r_dis[1]-n_dis[1])
            if(l == r) :
                if(hand =='right'):
                    answer += 'R'
                    right = num
                else:
                    answer += 'L'
                    left = num
            elif(l < r):
                answer += 'L'
                left = num
            elif(r < l):
                answer += 'R'
                right = num
    return answer

def find_index(num):
    keypad = [[1,2,3], [4,5,6],[7,8,9],[-1,0,-2]]
    for i in range(4):
        if(num in keypad[i]):
            return [i,keypad[i].index(num)]

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right")