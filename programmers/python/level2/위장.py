from itertools import combinations

def solution(clothes):
    catalog = {}
    for i in range(len(clothes)):
        if(clothes[i][1] in catalog):
            temp = catalog[clothes[i][1]]
            temp.append(clothes[i][0])
            catalog[clothes[i][1]] = temp
        else:
            catalog[clothes[i][1]] = [clothes[i][0]]
    print(catalog)
    num = []
    for i in catalog:
        num.append(len(catalog[i]))
    print(num)
    answer = 0
    for i in range(1,len(catalog)+1):
        if(i ==  1):
            answer += sum(num)
            continue
        count = list(combinations(num, i))
        for c in count:
            n = 1
            for i in c:
                n*= i
            answer += n
    return answer

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))