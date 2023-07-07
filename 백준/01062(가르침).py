""" 
김지민 선생님 K개 글자를 가르침
최대 단어...?
anta --- tica
"""
from sys import stdin
from itertools import combinations

N, K = map(int, input().split())

words = []
for _ in range(N):
    words.append(set(stdin.readline().rstrip()[4:-4]).difference('a', 'c', 'i', 't', 'n')) # anta, tica를 제외한 문자 저장

# a/c/i/t/n을 제외한 알파벳 모음 만들기
extra_word = set(ascii_lowercase).difference('a', 'c', 'i', 't', 'n') # 줄이기!! -> 21글자 필요X

if K < 5: # anta, tica는 5개가 넘기 때문에
    print(0)
elif K  == 26: # 전체 알파벳 수가 26개이기 때문에
    print(N)
else:
    # 최대 글자 찾기
    for x in list(combinations(extra_word, K - 5)):
        count = 0
        for word in words:
            if not word.difference(x):
                count += 1
        max_count = max(max_count, count)
    print(max_count)
