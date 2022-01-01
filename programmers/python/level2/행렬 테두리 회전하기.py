"""
직사각형 모양의 범위를 여러 번 선택 -> 시계방향으로 회전



"""
# 직사각형을 시계방향으로 돌리는 함수
## return 회전된 보드, 가장 작은 수
def rotate(board, query):
    check_num = board[query[0]-1][query[1]-1]
    loc = [query[0]-1, query[1]-1]
    min_num = check_num
    r_cnt, c_cnt = query[3]-query[1], query[2]-query[0]

    # 왼쪽
    for i in range(r_cnt):
        loc[1] += 1
        now_num = board[loc[0]][loc[1]]
        board[loc[0]][loc[1]] = check_num
        check_num = now_num
        min_num = min(min_num, check_num)
    print_board(board) 
    print(loc)
    # 아래
    for i in range(c_cnt):
        loc[0] += 1
        now_num = board[loc[0]][loc[1]]
        board[loc[0]][loc[1]] = check_num
        check_num = now_num
        min_num = min(min_num, check_num)
    print_board(board)
    print(loc)
    # 오른쪽
    for i in range(r_cnt):
        loc[1] -= 1
        now_num = board[loc[0]][loc[1]]
        board[loc[0]][loc[1]] = check_num
        check_num = now_num
        min_num = min(min_num, check_num)
    print_board(board)
    print(loc)
    # 위
    for i in range(c_cnt):
        loc[0] -= 1
        now_num = board[loc[0]][loc[1]]
        board[loc[0]][loc[1]] = check_num
        check_num = now_num
        min_num = min(min_num, check_num)

    return board, min_num

def print_board(board):
    print('==')
    for b in board:
        print(b)

def solution(rows, columns, queries):
    answer = []
    
    # 초기 보드 만들기
    board = []
    num = 1
    for i in range(rows):
        data = []
        for j in range(columns):
            data.append(num)
            num += 1
        board.append(data)
    
    # 시계 방향으로 회전시키기
    for q in queries:
        print('----------------')
        board, min_num = rotate(board, q)
        print_board(board)
        answer.append(min_num)
    return answer

print(solution(100, 97, [[1,1,100,97]]))