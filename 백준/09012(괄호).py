# 09012 괄호
import sys
from collections import deque

def input_func():
    input_data = sys.stdin.readline
    N = int(input_data())
    data = [input_data() for _ in range(N)]
    return N, data

def solution(N, data):
    for ele in data:
        
        # 하나의 케이스씩 확인
        stack = deque()
        for d in ele:
            if d == "(":
                stack.append("(")
            elif d == ")":
                if stack:
                    stack.pop()
                else:
                    print("NO")
                    break
        else:
            if not stack:
                print("YES")
            else:
                print("NO")


# 입력
N, data = input_func()

# 출력
solution(N, data)
