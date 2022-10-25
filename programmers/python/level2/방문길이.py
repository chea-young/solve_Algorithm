def solution(dirs):
    # 초기 설정
    direction = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R":(1, 0)}
    loc = (0, 0)
    route = [] # set(출발위치, 끝위치)
    
    # 명령어 수행하기
    for d in dirs:
        ## 다음에 갈 위치 계산하기
        nd = direction[d]
        nloc = (loc[0]+nd[0], loc[1]+nd[1])
        
        ## 좌표평면 안 인경우
        if -5<=nloc[0]<=5 and -5<=nloc[1]<=5:
            nroute = {loc, nloc}
            
            ### 새로운 길인 경우
            if nroute not in route:
                route.append(nroute)
            
            ### 이동
            loc = nloc
    return len(route)
