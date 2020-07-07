def solution(board, move):
    answer = 0
    basket = []

    for m in move:
        len_board = len(board)
        for index in range(len_board):
            check = True
            if( board[index][m-1] == 0):
                continue
            doll = board[index][m-1]
            if( basket != [] and basket[-1] == doll):
                check = False
                answer += 2
                basket.pop()
            board[index][m-1] = 0
            if(check):
                basket.append(doll)
            break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
move = [1,5,3,5,1,2,1,4]

print(solution(board,move))