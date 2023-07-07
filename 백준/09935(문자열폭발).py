#9935 문자열폭발

"""
폭발 문자 -> 폭발 -> 합쳐짐
과정
    존재 0 -> 
        모든 폭발 문자 폭발 -> 남은 문자열 합체
    존재 X -> 반복 


mdklC4dlkjC44
C4
-> 앞에 부분 for문 돌게 터뜨린 -> index 당기기
"""

# 폭발 문자열을 폭발 시키는 함수
def check_bomb(word, bomb):
    now = 0 # 현재 비교하는 첫 번째 index
    len_bomb = len(bomb)
    while now < len(word) - len_bomb + 1:
        if word[now:now+len_bomb] == bomb:
            word  = word[:now] + word[now+len_bomb:]
        else:
            now += 1
    return word

# 입력
word = input()
bomb = input()

while True:
    # 폭발 문자열 확인
    now_word = check_bomb(word, bomb)

    # 출력
    if not word: # 남아있는 문자가 없는 경우
        print("FRULA")
        break
    elif now_word == word: # 폭발 문자열이 없는 경우
        print(now_word)
        break

    word = now_word