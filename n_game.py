def solution(n, t, m, p):
    answer = ''
    num_str = ''
    for i in range(2*t):
        num_str += make_num(n, i)
        if(len(num_str) > 2*t):
            break
    print(num_str)
    for i in range(t):
        answer += num_str[p-1+i*m]
    return answer

def make_num(n, number):
    if(n == 10):
        return str(number)
    elif(n == 2):
        return str(bin(number))[2:]
    elif(n == 8):
        return str(oct(number))[1:]
    elif(n == 16):
        return str(hex(number))[2:].upper()

#print(solution(2,4,2,1))
print(solution(16,16,2,1))
#print(solution(16,16,2,2))