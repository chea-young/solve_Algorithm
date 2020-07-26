from itertools import permutations

def solution(numbers):
    list_num = [num for num in numbers]
    num = []
    for i in range(1,len(list_num)+1):
        num += list(permutations(list_num,i))
    number = []
    for n in set(num):
        a =''
        for j in n:
            a+= j
        if(find_decimal(int(a))):
            number.append(int(a))
    return len(set(number))       
        
def find_decimal(num):
    if(num == 1 or num == 0):
        return False
    for i in range(2,num):
        if(num%i ==0):
            return False
    return True

print(solution("17"))
print(solution("011"))