def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        map = []
        m1 = str(bin(arr1[i]))[2:]
        m1 = '0'*(n-len(m1)) +m1
        m2 = str(bin(arr2[i]))[2:]
        m2 = '0'*(n-len(m2)) +m2
        for j in range(n):
            if(m1[j]== '0' and m2[j] == '0'):
                map.append(' ')
            else:
                map.append('#')
        answer.append(''.join(map))
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))