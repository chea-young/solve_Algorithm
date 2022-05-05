# 01158 요세푸스 문제

# N명 
# K 번째 사람 제거

# 입력
N, K = map(int, input().split())
answer = []
data = [i+1 for i in range(N)]
now = 0
check_num = 1
while data:
    plus_in = now + K -1
    del_in = plus_in%len(data)
    check = plus_in//len(data)
    answer.append(data[del_in])
    del data[del_in]
    
    if check == 0:
        now= (now+1)%len(data)
        
# 출력
print(f'<{", ".join(map(str, answer))}>')
