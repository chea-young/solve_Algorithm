# 윷놀이 2490

# 도A(배1, 등3) 개B(배2, 등2) 걸C(배3, 등1) 윷D(배4) 모E(등4)
# 배0 등1

# 입력
info = {(1, 3): 'A', (2, 2): 'B', (3, 1): 'C', (4, 0): 'D', (0, 4): 'E'}
for i in range(3):
    data = [int(j) for j in input().split()]
    # 출력
    print(info[(data.count(0), data.count(1))])
