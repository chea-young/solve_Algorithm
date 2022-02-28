# 수 이어 쓰기 2 - 1790

# 입력
N, k = map(int, input().split())
digit = 1
nine = 9
answer = 0

#k 위치 구하기
while k > digit*nine:
    k = k - (digit*nine) # 이전 부분 제거
    answer = answer + nine
    # 자릿 수 추가
    digit += 1
    nine = nine * 10

answer = (answer+1) + ((k-1)//digit)
if answer > N:
    print(-1)
else:
    print(str(answer)[(k-1)%digit])
