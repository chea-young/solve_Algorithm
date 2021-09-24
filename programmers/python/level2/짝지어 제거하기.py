import numpy as np

def solution(s):
    return remove_word(np.array(s))

def remove_word(word):
    print(word)
    pre_word = ""
    del_list = []
    for i in range(word.size):
        if word[i] == pre_word:
            del_list.append(i)
            del_list.append(i-1)
            pre_word = ''
        else: 
            pre_word = word[i]
    if del_list :
        np.delete(word, del_list)
    else: 
        if word == []:
            return 1
        else:
            return 0

print(solution("baabaa"))