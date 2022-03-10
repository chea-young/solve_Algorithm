# 1009 분산처리

#입력
T = int(input())
"""
1 -> 1
2 -> 2, 4, 6, 8
3 -> 3, 9, 7, 1
4 -> 4, 6
5 -> 5
6 -> 6
7 -> 7, 9, 3, 1
8 -> 8, 4, 2, 6
9 -> 9, 1
10 -> 0

"""
for i in range(T):
    a, b = map(int, input().split())
    ele = a % 10
    if ele == 0:
        print(10)
    elif ele in [1, 5, 6]:
        print(ele)
    elif ele in [4, 9]:
        if b%2 == 0:
            print(ele*ele%10)
        else:
            print(ele)
    else:
        if b%4 == 0:
            print(ele**4%10)
        else:
            print(ele**b%4%10)
