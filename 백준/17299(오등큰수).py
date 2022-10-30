# 17299 오등큰수
import sys

"""
오등큰수 X -> -1


"""


def input_func():
    input_data = sys.stdin.readline
    N = int(input_data())
    nums = list(map(int, input_data().split()))
    return N, nums

def solution(N, nums):
    # 숫자가 등장한 횟수 찾기
    num_cnt = {} # 해당 숫자의 갯수를 찾는 리스트
    for n in nums:
        num_cnt[n] = num_cnt.get(n, 0) +1
    
    answer = [-1] * N
    max_num = (0, 0) # 숫자, 등장한 횟수
    for i in range(N-1, -1, -1):
        ncnt = num_cnt[nums[i]]
        temp = max_num[1] - ncnt
        if max_num[0] != 0 and temp > 0:
            answer[i] = temp
        
        if max_num[1] <= ncnt:
            max_num = (nums[i], ncnt)
    return answer
    
    
# 입력
N, nums = input_func()

# 출력
print(*solution(N, nums), end=" ")
