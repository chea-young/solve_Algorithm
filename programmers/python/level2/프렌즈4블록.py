def solution(m, n, board):
    board=[list(ele) for ele in board]
    while True:
        remove_b = find_puzzle(m, n, board)
        if remove_b == []: break
        board = remove_block(board, remove_b)
        board = change_loc(m, n, board)
    return count_answer(board)

def find_puzzle(m, n, board):
    remove_b = []
    m_index = 0 # 행
    n_index = 0 # 열
    
    while m_index != m:
        check = board[m_index][n_index]
        try: 
            if check != 0 and check == board[m_index][n_index+1] == check == board[m_index+1][n_index] == check == board[m_index+1][n_index+1]:
                remove_b += [(m_index, n_index), (m_index, n_index+1), (m_index+1, n_index), (m_index+1, n_index+1)]
        except IndexError:
            pass
            
        if n_index + 1 == n:
            m_index += 1
            n_index = 0
        else:
            n_index += 1
            
    return remove_b

def remove_block(board, remove_list):
    for ele in remove_list:
        board[ele[0]][ele[1]] = 0
    return board

def change_loc(m, n, board):
    m_index = m-1 # 행
    n_index = n-1 # 열
    while m_index != -1:
        if board[m_index][n_index] == 0:
            for num in range(m_index, -1, -1):
                if board[num][n_index] != 0:
                    board[m_index][n_index] = board[num][n_index]
                    board[num][n_index] = 0
                    break
        if n_index - 1 == -1:
            m_index -= 1
            n_index = n-1
        else:
            n_index -= 1
    return board

def count_answer(board):
    num = 0 
    for ele in board:
        num += ele.count(0)
    return num

def test():
    assert solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]) == 14
    assert solution(6, 6, 	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15

