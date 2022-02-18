# 싸이버개강총회
import sys
input = sys.stdin.readline
# 입력 0000 ex 23:14 -> 2314
start, end_event, end_stream = [int(i[:2] + i[3:]) for i in input().split()]
input_time = 0
in_list = set()
out_list = set()
while True:
    try:
        ele = input().split()
        input_time = int(ele[0][:2] + ele[0][3:])
        name = ele[1]
        
        if input_time <= start: # 개강총회를 시작하기 전에 들어온 인원
            in_list.add(name)
        elif end_event <= input_time <= end_stream: # 개강총회를 끝내고 나서, 스트리밍을 끝낼 때까지 인원
            out_list.add(name)
    except:
        print(len(in_list & out_list)) # 출력
        break      
