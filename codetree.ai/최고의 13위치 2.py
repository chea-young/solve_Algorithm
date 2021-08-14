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

def check_overlap(ele1, ele2):
    if ele1[1] != ele2[1]:
        return ele1[0] + ele2[0]
    if ele1[2]+3 <= ele2[2]:
        return ele1[0] + ele2[0]
    else:
        return None

check = []
def find_maxnum(first, second, maxnum):
    global check
    if first == second and first+1 == len(check):
        return maxnum
    elif second+1 == len(check):
        return find_maxnum(first+1, 0, maxnum)
    elif first == second:
        return find_maxnum(first, second+1, maxnum)    
    else:
        temp = check_overlap(check[first], check[second])
        if temp != None:
            maxnum = max(maxnum, temp)
        return find_maxnum(first, second+1, maxnum)

for col in range(num):
    for row in range(num):
        temp = check_num(col, row)
        if temp == None:
            break
        check.append((temp, col, row))

maxnum = find_maxnum(0, 1, 0)
print(maxnum)
