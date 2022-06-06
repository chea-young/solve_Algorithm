# 1202 보석도둑

# 보석 N개 -> M, V
# 가방 K개 -> C

#입력
N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

# 정렬
jewels.sort()
bags.sort()

# 가방의 무게보다 작거나 같은 보석에서 최대 가치인 보석 찾기
answer = 0
for b in bags:
    max_data = [] # (index, value)
    for i, j in enumerate(jewels):
        m, v = j
        if m <= b:
            if not max_data or max_data[1] < v:
                max_data = [i, v]
    answer += max_data[1]
    del jewels[max_data[0]]

# 출력
print(answer)
