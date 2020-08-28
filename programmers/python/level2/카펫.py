def solution(brown, yellow):
    if(find_decimal(yellow)):
        return [yellow+2,3]
    else:
        for i in range(1,yellow):
            if(yellow%i ==0):
                first = i+2
                second = yellow//i+2
                b = (first)*(second)
                if(brown+yellow ==b):
                    if(first>second):
                        return [first,second]
                    return [second,first]

def find_decimal(num):
    for i in range(2,num):
        if(num%i ==0):
            return False
    return True

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))