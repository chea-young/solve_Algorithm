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
        for ans in answer:
            if(i in ans):
                in_check = True
                break
        if(in_check):
            continue
        add = [i]
        out_check = True
        for c in connect:
            if(i in c):
                if(c[0] == i):
                    if(check[c[1]] ==-1):
                        add.append(c[1])
                        check[c[1]]=(count)
                        check[c[0]]=(count)
                        count += 1
                    else:
                        out_check = False
                        temp = answer[check[c[1]]]
                        temp.append(c[0])
                        answer[check[c[1]]] = temp
                        check[c[0]] = check[c[1]]
                else:
                    if(check[c[0]] ==-1):
                        add.append(c[0])
                        check[c[0]] = count
                        check[c[1]] = count
                        count +=1
                    else:
                        out_check = False
                        temp = answer[check[c[0]]]
                        temp.append(c[1])
                        answer[check[c[0]]] = temp
                        check[c[1]] = check[c[0]]
        if(out_check):
            answer.append(add)
    print("answer", answer)
    return len(answer)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))