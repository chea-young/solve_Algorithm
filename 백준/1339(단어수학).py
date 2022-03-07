# 1339 단어 수학

# ABCDEFG -> 숫자를 최대로 만들어서 계산
# 높은 자릿 수 대로 기록 A -> 10000 B 1000 이케!

# 입력
N = int(input())
word = []
dic_loc = {} # 알파벳 최대 자릿수를 넣는 dict
for i in range(N):
    w = input()
    word.append(w)
    for i, ele in enumerate(w):
        if ele not in dic_loc.keys():
           dic_loc[ele] = int('1'+'0' * (len(w)-i))
        else:
            dic_loc[ele] = dic_loc[ele] + int('1'+'0' * (len(w)-i))

tu_word = sorted(list(dic_loc.items()), key = lambda x: x[1], reverse=True) # 자릿수가 큰 숫자대로 정렬
digit = 9
dic_word = {} # 알파벳에 부여된 숫자 dict
for ele in tu_word:
    dic_word[ele[0]] = str(digit)
    digit -= 1
    
num = [] # 더해야하는 숫자 리스트
for ele in word:
    data = ''
    for c in ele:
        data += dic_word[c]
    num.append(int(data))

# 출력
print(sum(num))
