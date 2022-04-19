#1316 그룹 단어 체커

# 입력
N = int(input())

def check_group(word):
    word_dict = set()
    check = word[0]
    word_dict.add(check)
    for i in word:
        if check != i:
            if i not in word_dict:
                check = i
                word_dict.add(i)
            else:
                return False
    return True

answer = 0
for i in range(N):
    if check_group(input()): # 그룹 단어인 경우
        answer += 1

# 출력
print(answer)
