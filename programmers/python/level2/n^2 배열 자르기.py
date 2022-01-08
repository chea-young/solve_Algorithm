def solution_1(n, left, right):
    # 빈배열 만들기
    twoD_array = [[0 for __ in range(n)] for _ in range(n)]
    
    # _| 모양으로 배열 채우기
    for i in range(1, n+1):
        now = [0, i-1] # 현재 채우고자 하는 배열 인덱스
        ## 아래로 채우기
        for j in range(i-1):
            twoD_array[now[0]][now[1]] = i
            now[0] += 1
        
        ## 왼쪽으로 채우기
        for j in range(i):
            twoD_array[now[0]][now[1]] = i
            now[1] -= 1
    
    # 필요한 1차원 배열 만들기 -> 행: 몫, 열: 나머지
    answer = []
    for i in range(left, right+1):
        row = i//n
        col = i%n
        answer.append(twoD_array[row][col])
    return answer

#-----------------------------------------------

# (row, col) -> max(row, col) +1 이 자신의 수

def solution(n, left, right):
    # 필요한 1차원 배열 만들기 -> 행: 몫, 열: 나머지
    answer = []
    for i in range(left, right+1):
        row = i//n
        col = i%n
        ## max(row, col) +1 넣기
        answer.append(max(row, col)+1)
    return answer