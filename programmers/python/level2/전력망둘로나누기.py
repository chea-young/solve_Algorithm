from collections import deque

def solution(n, wires):
    answer = n
    conn = {i+1: [] for i in range(n)}
    for ele in wires:
        conn[ele[0]] = conn[ele[0]] + [ele[1]]
        conn[ele[1]] = conn[ele[1]] + [ele[0]]
    
    for out in wires:
        new_conn = conn.copy()
        new = new_conn[out[0]][:]
        new.remove(out[1])
        new_conn[out[0]] = new
        new = new_conn[out[1]][:]
        new.remove(out[0])
        new_conn[out[1]] = new
        
        visited = [False] * (n+1)
        check = deque()
        check.append(1)
        visited[1] = True
        while check:
            now = check.popleft()
            for ele in new_conn[now]:
                if not visited[ele]:
                    check.append(ele)
                    visited[ele] = True
                    
        # 최소 갯수가 max인 것을 계속 answer과 비교
        count = visited.count(True)
        answer = min(answer, abs(n-2*count))
    return answer
