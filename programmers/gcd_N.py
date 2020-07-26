from math import gcd
def solution(arr):
    a = []
    for i in range(0,len(arr),2):
        if(i == len(arr)-1):
            a.append(arr[i])
            break
        a.append(less_num(arr[i],arr[i+1]))
    if(len(a) == 2):
        return less_num(a[0],a[1])
    else:
        return solution(a)

def solution(arr):
    num = arr[0]
    for i in range(1, len(arr)):
        num = num//gcd(num,arr[i])*arr[i]
    return num

def less_num(n1,n2):
    num = gcd(n1,n2)
    return n1//num*n2
    

print(solution([2,6,8,14]))
print(solution([1,2,3]))