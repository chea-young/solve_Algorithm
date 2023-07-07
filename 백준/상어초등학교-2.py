#21608 상어 초등학교
import sys

N=int(input().rstrip())
student = {} #학생: [좋아하는 학생]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 학생 수 입력 
for _ in range(N*N):
    temp = list(map(int, input().split()))
    student[temp[0]] = temp[1:]

board = [[0 for _ in range(N)] for _ in range(N)]

# 주위 빈칸과, 인접해 있는 친구들를 담은 List 반환
def checkLoc(y,x):
    near=[]
    empty=0
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if not (0<=ny<N and 0<=nx<N):
            continue
        if board[ny][nx] > 0:
            near.append(board[ny][nx])
        else:
            empty+=1
    return near,empty

# 학생을 넣을 자리를 찾는 리스트
def findLoc(l):
    l.sort()
    friend,empty,y,x = l[0]
    return y,x
    

# 학생들 자리 구하기
for i in student.keys():
    ## 비어 있는 자리에 대한 데이터 구하기
    locList = []
    for y in range(N):
        for x in range(N):
            if board[y][x]: ### 학생으로 이미 채워져 있는 경우
                continue

            likeCnt=0
            near,empty = checkLoc(y, x) ### 인점한 학생, 인접한 비어있는 칸 수
            
            for like in student[i]: ### 주변 좋아하는 학생 수 증가
                if like in near:
                    likeCnt+=1

            locList.append([-likeCnt, -empty, y, x])

    ## 학생들 리스트에 넣기
    y,x = findLoc(locList)
    board[y][x] = i

# 만족도 구하기
ans=0
score=[0,1,10,100,1000]
for i in range(N):
    for j in range(N):
        cnt=0
        friendList=checkLoc(i,j)[0]
        # 인접하는 좋아하는 학생 주의 따라 점수 계산하기
        for friend in friendList:
            if friend in student[board[i][j]]:
                cnt+=1
        ans+=score[cnt]

# 출력
print(ans)