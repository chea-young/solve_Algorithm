# 2671 잠수함식별

""" 
re.compile -> 해당 문자열 패턴 생성
fullmatch -> 생성한 문자열 패턴에 대해 규칙이 맞는지 확인


"""
import re

# 입력
str_submarine = input()

# 패턴 생성
p = re.compile('(100+1+|01)+')

# 출력
if p.fullmatch(str_submarine):
    print("SUBMARINE")
else:
    print("NOISE")