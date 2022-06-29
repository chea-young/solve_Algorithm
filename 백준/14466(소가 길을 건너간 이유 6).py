# 14466(소가 길을 건너간 이유 6)

"""
K 마리의 소
소는 각자 다른 목초지
길을 건너지 X 못 만남



"""
# 입력
N, K, R = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(R)]
loc = [list(map(int, input().split())) for _ in range(K)]