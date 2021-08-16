# 안겹치게 추가하기! - 1000 그거 해보기
# 아니면 그 다음 조랍 찾기
num = int(input())
grid = [[0 for i in range(num)] for j in range(num)]

for col in range(num):
    n = list(map(int, input().split()))
    grid[col] = n

def check_num (col, row):
    global grid
    count = 0
    if row+3 > num:
        return None
    for i in range(3):
        if grid[col][row+i] == 1:
            count +=1
    return count


check = []
for col in range(num):
    for row in range(num):
        temp = check_num(col, row)
        if temp == None:
            break
        check.append(temp)
        
check = sorted(check)
print(check[-1] + check[-2])