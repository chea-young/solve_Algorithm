def solution(n):
    num = n**(0.5)
    if(int(num)-num == 0):
        return (int(num)+1)**2
    else:
        return -1

print(solution(121))
print(solution(3))