def solution(w,h):
    gcd = 0
    for i in range(min(w,h),0,-1):
        if(w%i == 0 and h%i ==0):
            gcd = i
            break
    return w*h-gcd*(w//gcd+h//gcd-1)

print(solution(8,12))
print(solution(2,3))