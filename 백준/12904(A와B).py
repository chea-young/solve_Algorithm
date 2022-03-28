# 12904 A와 B

# 두 문자열 S, T -> S를 T로 바꾸는 게임
## 연산
# 문자열 뒤에 A를 추가
# 문자열 뒤집기 + B 추가

# 입력
S = input()
T = input()

# 문자열 뒤에 A를 추가
def add_A(str):
    return str+'A'

# 문자열 뒤집기 + B 추가
def reverse_add_B(str):
    return str[::-1] + 'B'

# 연산
def calculation(str):
    global T, answer
    if str == T:
        answer = 1
    elif len(str) < len(T):
        calculation(add_A(str))
        calculation(reverse_add_B(str))
    
answer = 0
calculation(S)

# 출력
print(answer)
