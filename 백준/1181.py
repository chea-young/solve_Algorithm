#단어 정렬
num = int(input())
data = []
for i in range(num): # 입력
    ele = input()
    if ele not in data: data.append(ele)
    
data = sorted(data, key=lambda x : (len(x), x)) # 길이 순, 사전 순 정렬

for ele in data: # 출력
    print(ele)
