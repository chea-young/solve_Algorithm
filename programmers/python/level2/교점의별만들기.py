from itertools import combinations

# 두 직선의 모든 좌표가 정수인 교점 구하기
def intersection_point(line1, line2):
    a,b,e = line1
    c,d,f = line2
    if a*d == b*c: # 기울기가 같을 때
        return None
    x = (b*f-e*d)/(a*d-b*c)
    y = (e*c-a*f)/(a*d-b*c)
    if x == int(x) and y == int(y):
        return (int(x),int(y))

def solution(line):
    N = len(line)
    # 두 직선씩 짝지어 교점 구하기 
    cases = list(combinations(line,2))
    points = set()
    for comb in cases:
        point = intersection_point(comb[0], comb[1])
        if point:
            points.add(point)
            
    # 교점의 x좌표들 
    xs = [p[0] for p in points]
    x_min = min(xs)
    x_max = max(xs)
    
    # 교점의 y좌표들
    ys = [p[1] for p in points]
    y_min = min(ys)
    y_max = max(ys)
    
    # 모두 . 으로 초기화 
    answer = [['.' for _ in range(x_max-x_min+1)] for __ in range(y_max-y_min+1)]
    for point in points:
        x, y = point
        answer[y_max-y][x-x_min] = '*'
        
    return [''.join(ans) for ans in answer]
