from itertools import combinations
def solution(nums):
    answer = list(combinations(nums,3))
    check = []
    for tup in answer :
        number =sum(tup)
        check.append(number)
    ans = len(check)
    for i in check:
        for j in range(2,i):
            if(i%j == 0):
                ans -= 1
                break
    return ans

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
print(solution([2,6,4]))

