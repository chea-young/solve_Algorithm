# 20056 마법사 상어와 파이어볼

# d 방향으로 s칸 만큼 이동
# 2개 이상의 파이어볼이 있으면
    # 같은 칸 하나로 합쳐짐
    # 4개로 나누어집
    # 질량 /5, 속력 /개수 방향 

d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 입력
N, M, K = map(int, input().split())
data = [list(map(int, input().split())) for i in range(M)] #ri, ci, mi, si, di

for i in range(K):
    loc = {}
    # 파이어볼 계산
    for ri, ci, mi, si, di in data:
        ri = (ri + d[di][0] * si) % N
        ci = (ci + d[di][1] * si) % N
        if loc != {} and (ri, ci) in loc.keys():
            loc[(ri, ci)].append([mi, si, di])
        else:
            loc[(ri, ci)] = [[mi, si, di]]
    

    
    data = []
    # 겹쳐진 파이어볼 계산
    for keys, values in loc.items():
        if len(values) == 1:
            data.append([keys[0], keys[1]]+values[0])
            continue
        mi = sum([j[0] for j in values])//5
        if mi == 0: # 질량이 0이 되었을 때
            continue
        
        si = sum([j[1] for j in values])//len(values)
        di = 0
        di_state = 'even'
        if values[0][2]%2 == 1:
            di_state = 'odd'
        
        for j in values:
            if j[2]%2 == 0 and di_state == 'even':
                continue
            elif j[2]%2 == 1 and di_state == 'odd':
                continue
            else:
                di_state = False
                break
        
        if not di_state:
            di = [1, 3, 5, 7]
        else:
            di = [0, 2, 4, 6]
            
        for di_ele in di:
            data.append([keys[0], keys[1], mi, si, di_ele])
            
# 모든 질량 계산
answer = sum([i[2] for i in data])
print(answer)
