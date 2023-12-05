# 01563 개근상
import sys
from functools import cmp_to_key

"""
알파벳 20
a b c d e f g h i j k l m n o p q r s t u v w x y z
민식어 
a b k d e g h i l m n ng o p r s t u w y
- 순서 다름
- 

민식어가 주어졌을 때, 순서대로 정렬하는 프로그램
"""

def input_data():
    input_func = sys.stdin.readline
    N = int(input_func())
    word_list = [input_func().split()[0] for _ in range(N)]
    return N, word_list

def solve(N, word_list):
    result = dict() # {원래 str: 변경된 str}
    for i in word_list: 
        changed_word = changeMinSick(i)
        result[i] = changed_word
    
    return sorted(result.items(), key= lambda x : x[1]) # item 기준으로 정렬!! 

def changeMinSick(word) :
    result = word.replace("ng", "L")
    for k, v in MIN_SICK_WORD.items() :
        result = result.replace(k, v)
    return result

# 입력
N, word_list = input_data()
MIN_SICK_WORD = {"a": "A", "b": "B", "k":"C",
            "d": "D", "e":"E", "g":"F", 
            "h":"G", "i":"H", "l":"I",
            "m":"J", "n":"K",
            "o":"M", "p":"N", "r":"O",
            "s":"P", "t":"Q", "u":"R",
            "w":"S","y":"T"
            }

# 출력
answer = solve(N, word_list)
for key, value in answer:
    print(key)

##=====================================##

def solve_1(N, word_list):
    # init
    word_list.sort(key=cmp_to_key(compare))
    
    return word_list

def compare(x, y):
    len_x = len(x)
    len_y = len(y)
    cnt = max(len_x, len_y)
    
    for i in range(cnt):
        str_x = x[i] if i < len_x-1 else ""
        str_y = y[i] if i < len_y-1 else ""
        
        if str_x == "": # "" 인 경우는 다른 문자보다 길이가 더 짧은 것을 의미 -> 우선순위가 올라감
            return -1
        elif str_y == "":
            return True
        else: # 고려 필요
            pass
    
    if x[0]<y[0]:
        return True
    elif x[0] == y[0]:
        return 0
    else:
        return -1
   
