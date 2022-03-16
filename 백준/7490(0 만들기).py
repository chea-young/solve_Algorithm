# 7490 0 만들기

# 입력
T = int(input())
for _ in range(T):
    num = int(input())
    # 모든 경우의 수 구하기
    all_data = ['1']
    for n in range(2, num+1):
        data = []
        for m in ['+', '-', ' ']: # 모든 숫자에 대한 모든 경우의 수들을 추가
            for ele in all_data:
               data.append(ele+m+str(n))
        all_data = data
    
    answer = []
    # 식 계산하기
    for ele in all_data:
        cal = ele.replace(' ','') # 계산을 위해 문자열 변경
        if eval(cal) == 0:# eval : 문자열 식의 합을 구하는 모듈
            answer.append(ele)
    
    # ASCII 순서로 정렬
    answer = sorted(answer)
    for ele in answer:
        print(ele) # 출력
