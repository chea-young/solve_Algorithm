# 18869 멀티버스2

"""
회문 : 앞 뒤 방향으로 같은 순서의 문자로 구성
한 문자를 삭제하여 회문 생성가능 문자열 -> 유사회문
?회문 0, 유사회문 1, 일반 문사열 2

"""

"""

a b b c b d a
0 1 2 3 4 5 6
7 6 5 4 3 2 1

"""
import sys

sys.stdin = open('input/17609.txt')

def input_data():
    input_func = sys.stdin.readline
    N = int(input_func())
    word_list = [input_func().split()[0] for _ in range(N)]
    return N, word_list

def solve(N, word_list):
    answer = []

    # 문자열 상태 확인
    for word in word_list:
        ## 회문 혹은 유사 회문 확인
        result = check_palindrome(word)
        answer.append(result)
    return answer

def check_palindrome(word, is_deleted = False):
    count = len(word)//2 # 대칭인 만큼 확인
    for i in range(count):
        if word[i] == word[(-1) * (i+1)]: # 앞 뒤가 같은 경우
            continue
        else: # 앞 뒤가 다른 경우
            if is_deleted: # 하나를 삭제했는데도 불구하고 대칭이 아닌 경우
                return 2
            else:
                # 앞의 다른 문자 삭제
                result = check_palindrome(word[0:i]+word[i+1:], True)

                # 뒤의 다른 문자 삭제
                if result == 2:
                    back_i = len(word) - i - 1
                    return check_palindrome(word[0:back_i]+word[back_i+1:], True)
                else:
                    return 1

    # 대칭
    if is_deleted: # 한 문자가 삭제 -> 유사 회문
        return 1
    else: # 회문
        return 0

# 입력
N, word_list = input_data()

# 출력
print(*solve(N, word_list), sep="\n")

"""
0
1
1
2
2
0
1
"""