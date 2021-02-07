
def solution(numbers):
    if(sum(numbers) == 0):
        return '0'
    num = [str(i) for i in numbers]
    answer = sorted(num, key=lambda x: x*3, reverse=True)
    return ''.join(answer)

#print(solution([6,10,2]))
#print(solution([3, 30, 34, 5, 9]))
#print(solution([0,0,0,0,0]))
#print(solution([242,424,242]))
#print(solution([1,2,22,3,4,5,6,7,8]))
print(solution([12,121]))
print(solution([12,122]))
print(solution([21, 212]))
print(solution([999,9,998]))
print(solution([1000,10,100]))
print(solution([344,34,3]))
# 다른 문제 풀이
from functools import cmp_to_key

def compare(x, y):
    if x + y < y + x:
        return 1
    else:
        return -1

def solution(numbers):
    numbers = map(str, numbers)
    numbers = sorted(numbers, key=cmp_to_key(compare))
    answer = ''.join(numbers)
    if answer[0] == '0':
        answer = '0'
    return answer