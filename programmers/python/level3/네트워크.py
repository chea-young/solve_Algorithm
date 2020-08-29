def solution(n, computers):
    connect = []
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if(computers[i][j]==1):
                if(i == j):
                    continue
                elif(i<j):
                    if([i,j] not in connect): 
                        connect.append([i,j])
                else:
                    if([j,i] not in connect):
                        connect.append([j,i])
    connect.sort()
    check = [-1]*n
    count = 0
    print("connect",connect)
    answer = []
    for i in range(n):
        in_check = False
        if(check[i] != -1):
            continue
        add = [i]
        out_check = True
# 오류 없음
        for c in connect:
            if(i in c):
                out_check = False
                if(c[0] == i):
                    if(check[c[1]] ==-1):
                        add.append(c[1])
                        check[c[1]]=(count)
                        check[c[0]]=(count)
                        count += 1
                        answer.append(add)
                    else:
                        answer[check[c[1]]].append(c[0])
                        check[c[0]] = check[c[1]]
                else:
                    if(check[c[0]] ==-1):
                        add.append(c[0])
                        check[c[0]] = count
                        check[c[1]] = count
                        count +=1
                        answer.append(add)
                    else:
                        answer[check[c[0]]].append(c[1])
                        check[c[1]] = check[c[0]]
        if(out_check):
            answer.append(add)
            
    print("answer", answer)
    return len(answer)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))