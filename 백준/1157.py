# 단어공부
word = {}
max_str = (0, 0) # 가장 빈도 높은 알파벳, 빈도수
# 입력
for ele in input().upper():
    if ele not in word.keys(): # 문자의 빈도 수 추가
       word[ele] = 1
    else:
        num = word[ele]
        word[ele] = num+1
        if max_str[1] < num+1: max_str = (ele, num+1)
#출력
if list(word.values()).count(max_str[1]) > 1: # 최대 빈도 수의 숫자가 같은 것이 있는 경우
    print('?')
else:
    print(max_str[0])
