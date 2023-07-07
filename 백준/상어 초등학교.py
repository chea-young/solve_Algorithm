#21608 상어 초등학교

"""
|r1 - r2| + |c1 - c2| = 1 -> 인접하다

인접한 캄 중 가장 많은 칸으로 자리
"""

# 입력
N = int(input())
data = {}
for i in range(N**2):
    ele = map(int, input().split())
    data[ele[0]] = set(ele[1:])

# 인점 비어있는 리스트 갯수 찾기
adjList = [] #(-개수, 행, 열)
for i in range(N):
    for j in range(N):
        if i in [0, N-1] and j in [o, N-1]:
            adjList.append(-2, i, j)
        elif i in [0, N-1] and j in [o, N-1]:
            adjList.append(-3, i, j)
        else:
            adjList.append(-4, i, j)
adjList.sort()

inStuList = {} # 채워진 자리 학생 dict
inLocList = set() # 채워진 자리 index set

# 학생들 자리 넣기
for s, favStu in data.items():
    ## 좋아하는 학생 중 채워진 학생
    inFavStu = []
    if not inStuList:
        inFavStu = inLocList - data[s]
    
    ### 좋아하는 학생 중 채워진 학생이 없는 경우
    if not inFavStu:
        check = adjList.pop(0)
        check = (check[1], check[2])
        inStuList[s] = check
        inLocList.add(check)
    ### 좋아하는 학생 중 채워진 학생이 있는 경우
    
# 출력
