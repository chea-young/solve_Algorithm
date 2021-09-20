def solution(s):
    dict_word = {"zero":'0', "one":'1', "two":'2', "three": '3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight": '8', "nine":'9'}
    word = ''
    answer = ''
    for i in s:
        if word in dict_word.keys():
            answer += dict_word[word]
            word = ''
        if i.isdigit():
            answer += str(i)
        else:
            word += i
    if word in dict_word.keys():
        answer += dict_word[word]
    return int(answer)

#print(solution("one4seveneight"))
print(solution("23four5six7"))