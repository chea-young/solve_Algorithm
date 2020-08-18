def solution(cacheSize, cities):
    if(cacheSize ==0):
        return len(cities)*5
    cache = []
    answer = 0
    for i in range(len(cities)):
        c = cities[i].lower()
        try:
            ind = cache.index(c)
            answer +=1
            del cache[ind]
            cache.append(c)
        except ValueError:
            answer += 5
            if(len(cache) == cacheSize):
                cache.pop(0)
            cache.append(c)
    return answer

print(solution(3,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))
print(solution(2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA','SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA','SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(2,['Jeju', 'Pangyo', 'NewYork', 'newyork']))
print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))