num = int(input())
grid = [[0 for i in range(num)] for j in range(num)]

for col in range(num):
    n = list(map(int, input().split()))
    grid[col] = n

def comb(lst,n):
	ret = []
	if n > len(lst): return ret
	
	if n == 1:
		for i in lst:
			ret.append([i])
	elif n>1:
		for i in range(len(lst)-n+1):
			for temp in comb(lst[i+1:],n-1):
				ret.append([lst[i]]+temp)
	return ret

def find_p(element):
    if len(element) == 2:
        return grid[element[0]-1][element[1]-1] + grid[element[1]-1][element[0]-1]
    cal_list = comb(element, 2)
    cal = 0
    for i in cal_list:
        cal += grid[i[0]-1][i[1]-1] + grid[i[1]-1][i[0]-1]
    return cal

p = [i+1 for i in range(num)]
check_list = comb(p, num//2)
in_list = [] # 확인을 한 list

answer = 100
for element in check_list:
    if element in in_list:
        continue
    temp  = list(set(p) - set(element))
    in_list.append(temp)
    mor = find_p(element)
    nig = find_p(temp)
    answer = min(answer, abs(mor-nig))
print(answer)