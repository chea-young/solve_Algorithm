from collections import deque

def solution(tickets):
    answer = []
    conn = {} #공향: 가능한 공항

    # 방문 가능한 공항 찾기
    for a, b in tickets:
        conn[a] = conn.get(a, []) + [b]

    data = deque() # (공항, 방문한 경로, 사용하지 않은 티켓)
    data.append(("ICN", ["ICN"], tickets.copy()))
    while data:
        now, move, ticket = data.popleft()

        if not ticket: # 주어진 티켓을 모두 사용한 경우
            answer.append(move)

        if now not in conn.keys(): # 갈 수 있는 공항이 없는 경우
            continue

        for ele in conn[now]:
            if [now, ele] in ticket: # 가는 항공권이 있는 경우
                nextTicket = ticket.copy()
                nextTicket.remove([now, ele])
                data.append((ele, move+[ele], nextTicket))
    
    return sorted(answer)[0]
