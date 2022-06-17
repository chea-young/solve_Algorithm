def findCase(c, order): 
    case = []
    order = sorted(order)
    used = [0 for _ in range(len(order))]
 
    def generate(chosen):
        if len(chosen) == c:
            case.append(tuple(chosen.copy()))
 
        start = order.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(order)):
            if used[nxt] == 0 and (nxt == 0 or order[nxt-1] != order[nxt] or used[nxt-1]):
                chosen.append(order[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])
    return case
 
 
def solution(orders, course):
    answer = []
    # 가능한 메뉴 구성 구하
    orderCase = {c: [] for c in course} # {메뉴구성개수: [구성조합]}
    for order in orders:
        for c in course:
            # 원하는 조합의 개수보다 주문 수가 작은 경우 
            if len(order) < c:
                break
            
            # 구성 조합 구하기
            orderCase[c] += findCase(c, order)
    
    # 메뉴 불린 횟수 저장하기
    orderMenu = {} # {메뉴구성개수: {구성조합: 주문 수}}
    for c in course:
        caseCnt = {}
        for ele in orderCase[c]:
            caseCnt[ele] = caseCnt.get(ele, 0) + 1
        orderMenu[c] = caseCnt
    
    # 제일 많이 불린 음식 구하기
    orderMenuSorted = {c: sorted([(v, k) for k, v in orderMenu[c].items() if v > 1]) for c in course} # {메뉴구성개수: [주문수, 구성조합]}
    for c in course:
        cData = orderMenuSorted[c]
        bestCourse = []
        if cData:
            bestCourse =  cData.pop()
            answer.append(''.join(bestCourse[1]))
        while cData:
            if bestCourse[0] ==  cData[-1][0]:
                answer.append(''.join(cData.pop()[1]))
            else:
                break
            
    return sorted(answer)
