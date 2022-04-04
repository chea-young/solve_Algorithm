import itertools

def solution(k, dungeons):
    answer = 0
    case =  itertools.permutations(dungeons, len(dungeons)) # 모든 경우의 수 구하기
    
    for ele in case:
        energy = k
        count = 0
        for now, need in ele:
            if energy >= now:
                energy -= need
                count += 1
            else: break
        answer = max(count, answer) # 최대 던전 수로 변경
    return answer
