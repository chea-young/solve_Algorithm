def solution(numbers):
    # string 리스트로 바꾸기
    strNum = map(str, numbers)

    # 리스트 정렬하기
    sortedStrNum = sorted(strNum, key=lambda x : x*3, reverse=True)
    
    # 정렬된 리스트 합치기
    return ''.join(sortedStrNum)

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
