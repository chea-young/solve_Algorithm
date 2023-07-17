# 23843 콘센트
import sys
import heapq

sys.stdin = open("./input/01713.txt", "r")

"""
학생회장 후보 -> 전체 학생의 추천

규칙
1. 시작하기 전에는 비어있음
2. 특정 학생 추천 -> 반드시 사진틀에 게시
3. 비어있는 사진틀 없는 경우 -> (추천 수 작고, 오래된 사진) 학생 삭제 -> 새로운 학생 게시
4. 다른 학생의 추천 받은 경우 -> 추천받은 횟수 많큼 증가
5. 삭제되는 경우 -> 추천받은 횟수는 0
"""


def input_func():
    input_data = sys.stdin.readline
    N = int(input_data())
    total_cnt = int(input_data())
    student_list = list(map(int, input_data().split()))
    return N, total_cnt, student_list


def solution(N, total_cnt, student_list):
    # init
    recommendations_cnt = {}  # 학생 번호: (추천 받은 수 (삭제되면 지워짐), 순서)

    # 사진틀에 걸렸있는 후보 구하기
    for i, s_num in enumerate(student_list):
        data = [1, i, s_num]

        if (
            recommendations_cnt and s_num in recommendations_cnt.keys()
        ):  # 이전에 추천받은 적이 있는 경우
            recommendations_cnt[s_num][0] += 1

        else:  # 새롭게 추천받은 경우
            total_recommendations_data = list(recommendations_cnt.items())
            if len(total_recommendations_data) < N:  # 사진틀에 빈 공간이 있는 경우
                recommendations_cnt[s_num] = [1, i]
            else:  # 남은 공간이 없는 경우
                total_recommendations_data.sort(key=lambda x: (x[1][0], x[1][1], x[0]))
                del recommendations_cnt[total_recommendations_data[0][0]]

                recommendations_cnt[s_num] = [1, i]

    return sorted(list(recommendations_cnt.keys()))


# 입력
N, total_cnt, student_list = input_func()

# 출력
print(*solution(N, total_cnt, student_list))
