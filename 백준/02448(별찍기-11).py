# 2448 별 찍기 - 11

def print_star(y, x, n):
#   . -> y,x
#   *
#  * *
# *****
    if n ==3:
        data[y][x] = '*'
        data[y+1][x+1] = '*'
        data[y+1][x-1] = '*'
        for i in range(-2, 3):
            data[y+2][x+i] = '*'
    else:
        plus = n//2
        print_star(y, x, plus)
        print_star(y+plus, x+plus, plus)
        print_star(y+plus, x-plus, plus)

# 입력
N = int(input())
data = [[' ' for i in range(2*N)] for i in range(N)]
            
print_star(0, N-1, N)

# 출력
for ele in data:
    print("".join(ele))
