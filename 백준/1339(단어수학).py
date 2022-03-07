# 1339 단어 수학

# ABCDEFG -> 숫자를 최대로 만들어서 계산

# 입력
N = int(input())
word = []
for i in range(N):
    word.append(input())
word = sorted(word, key = lambda x: len(x), reverse=True)

num = [] # 더해야하는 숫자 리스트
dic_word = {} # 알파벳에 부여된 숫자 dict
digit = 9
# 알파벳에 번호 부여하기
for ele in word:
    data = ''
    for c in ele:
        if c not in dic_word.keys():
            dic_word[c] = str(digit)
            digit -= 1
        data += dic_word[c]
    num.append(int(data))

# 출력
print(sum(num))
            
