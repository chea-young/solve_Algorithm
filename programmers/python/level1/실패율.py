def solution(N, stages):
    n_clear = [stages.count(i+1) for i in range(N+1)]
    r_clear = [sum(n_clear[i:]) for i in range(N)]
    answer = []
    for i in range(N):
        try:
            answer.append((n_clear[i]/r_clear[i], -(i+1)))
        except ZeroDivisionError:
            answer.append((0,-(i+1)))
    answer = sorted(answer, key=lambda x:x[0], reverse=True)
    return [-i[1] for i in answer]

def solution1(N, stages):
    n_clear = [0]*N
    r_clear = [0]*(N)
    for i in stages:
        if(i == N+1):
            for j in range(N):
                r_clear[j]+=1
            continue
        n_clear[i-1] +=1
        for j in range(i):
            r_clear[j]+=1
    answer = sorted([(n_clear[i]/r_clear[i], -(i+1)) for i in range(N)], key=lambda x:x[0], reverse=True)
    return [-i[1] for i in answer]

def solution2(N, stages):
    answer = []
    for i in range(N):
        n_clear = stages.count(i+1)
        r_user = 0
        for j in stages:
            if(j-1>=i):
                r_user +=1
        answer.append((n_clear/r_user, -(i+1)))
    answer = sorted(answer, key=lambda x:x[0], reverse=True)
    return [-i[1] for i in answer]

a = solution2(5, [2, 1, 2, 6, 2, 4, 3, 3])
#print(a)
b = solution2(4, [4,4,4,4,4])
#print(b)

c = solution(5, [1,1,1,1,1])
print(c)
