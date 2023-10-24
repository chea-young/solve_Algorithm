# 22352 항체인식
import sys
from collections import deque

"""
격자의 칸 중 하나에 -> 항체 생성
현재 속해 있는 칸과 상하좌우 인점 -> 그 칸으로 -> 퍼질 X -> 완전히 스며듬 -> 동일한 값으로 업데이트

--->
숫자가 같은 칸을 부분을 업데이트 시켜주고 after과 같으면 됨.

전체를 비교하다가, 다른 값인 부분이 나오고 그 구역 부분이 동일하면 -> Yes
-> 다른 구역인 부분이 2번 이상이면 X
"""


def input_func():
    input_data = sys.stdin.readline
    N, M = map(int, input_data().split())
    before_board = [list(map(int, input_data().split())) for _ in range(N)]
    after_board = [list(map(int, input_data().split())) for _ in range(N)]
    return N, M, before_board, after_board


def solve(N, M, before_board, after_board):
    isDiff = False

    for i in range(N):
        for j in range(M):
            if before_board[i][j] != after_board[i][j]:
                if isDiff:
                    return "NO"  # 이마 한번 탐색했던 것.

                isDiff = True
                bfs(i, j)
    return "YES"


def bfs(y, x):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False] * M for _ in range(N)]

    q = deque([(y, x)])
    visited[y][x] = True
    before_value = before_board[y][x]
    after_value = after_board[y][x]
    while q:
        ny, nx = q.pop()
        before_board[ny][nx] = after_value

        for d in range(4):
            nny = ny + dy[d]
            nnx = nx + dx[d]

            if 0 <= nny < N and 0 <= nnx < M and not visited[nny][nnx]:
                if before_board[nny][nnx] == before_value:
                    visited[nny][nnx] = True
                    q.appendleft((nny, nnx))


# 입력
N, M, before_board, after_board = input_func()

# 출력
print(solve(N, M, before_board, after_board))
