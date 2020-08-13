def solution(n, computers):
    connect = []
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if(i == j):
                continue
            elif(i<j):
                if([i,j] not in connect): 
                    connect.append([i,j])
            else:
                if([j,i] not in connect):
                    connect.append([j,i])
    connect.sort()
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
        for c in connect:
            if(i in c):
                if(c[0] == i):
                    add.append(c[1])
                else:
                    add.append(c[0])
    return len(answer)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))