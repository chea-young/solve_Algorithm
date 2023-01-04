# 18869 멀티버스2

"""
M개 우주 
N개 행성

균등한 우주 쌍이 몇 개인지

구성 0 -> 같은거 : 조합

[조건]

우주A, 우주 B 비교
[[A_i, B_i], ...] -> 0번 기준 정렬 -> 1번 인덱스가 점점 커지는지 비교
    - 만약에 같은 경우에만 0번 인덱스 비교


"""
import sys
from itertools import combinations

def input_data():
    input_func = sys.stdin.readline
    M, N = map(int, input_func().split())
    planet_list = [list(map(int, input_func().split())) for _ in range(M)]
    return M, N, planet_list

def solve(M, N, planet_list):
    # 초기 설정
    cnt = 0
    universe_case = list(combinations([i for i in range(M)], 2))

    # 우주의 조합별로 가능한지 구하기
    for case in universe_case:
        p_list = create_compare_list(case)

        ## 균등한지 확인 i, i+1 비교
        for i in range(N-1):
            if p_list[i][1] < p_list[i+1][1]: ### 균등: 조건 1
                continue
            elif p_list[i][1] == p_list[i+1][1]:
                if p_list[i][0] == p_list[i+1][0]:
                    continue ### 균등: 조건 2
                else:
                    break
            else:
                break
        else: # for문을 모든 행성에 대해서 다 잘 돈 경우
            cnt += 1
    
    return cnt
    
# 우주의 조합의 행성 리스트
def create_compare_list(case):
    p_list = []
    for i in range(N):
        a = planet_list[case[0]][i]
        b = planet_list[case[1]][i]
        p_list.append([a, b])
    return sorted(p_list)
    

# 입력
M, N, planet_list = input_data()

# 출력
print(solve(M, N, planet_list))