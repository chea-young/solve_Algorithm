def solution(lottos, win_nums):
    score = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6 }
    min_num = len(list(set(lottos) & set(win_nums)))
    max_num = 0
    zero_count = lottos.count(0)
    max_num= min_num+zero_count # 제로인 수가 정답이 될 수 있는거이기 때문에
    answer = [score[max_num], score[min_num]]
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))