def solution(sizes):
    # 정렬
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i] = [sizes[i][1], sizes[i][0]]
    
    # 길이 찾기
    w = 0
    h = 0
    for i in sizes:
        if i[0] > w:
            w = i[0]
        if i[1] > h:
            h = i[1]
    answer = w * h
    return answer
