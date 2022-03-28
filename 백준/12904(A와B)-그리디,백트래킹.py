# 12904 A와 B

# 두 문자열 S, T -> S를 T로 바꾸는 게임
## 연산
# 문자열 뒤에 A를 추가
# 문자열 뒤집기 + B 추가

# 입력
S = input()
T = input()

# 문자열 뒤에 A를 빼기
def delete_A(str):
    return str[:-1]

# B 빼기 + 뒤집기
def delete_B_reverse(str):
    str = str[:-1]
    if len(str) > 1:
        return str[::-1]
    else:
        return str

# 연산
def calculation(str):
    if str[-1] == 'A':
        return delete_A(str)
    elif str[-1] == 'B':
        return delete_B_reverse(str)
    
while True:
    T = calculation(T)
    if S == T:
        print(1)
        break
    elif len(S) >= len(T):
        print(0)
        break
