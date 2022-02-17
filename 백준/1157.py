# 단어공부
word = input().upper()
word_list = list(set(word))

max_str = (0, 0) # 가장 빈도 높은 알파벳, 빈도수
count_num = []
for ele in word_list:
    num = word.count(ele)
    count_num.append(num)
    if max_str[1] < num: max_str = (ele, num)
    
# 출력
if count_num.count(max_str[1]) > 1: # 최대 빈도 수의 숫자가 같은 것이 있는 경우
    print('?')
else:
    print(max_str[0])
