# 싸이버개강총회
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
        
        if input_time <= start: # 개강 총회 전에 들어온 인원
            in_list.add(name)
        elif input_time < end_event: # 개강 총회 끝나기 전에 나간 사람
            in_list.remove(name)
        else: # 개강 총회 끝나고 나가는 사람
            out_list.add(name)
            
    except:
        break      
print(len(in_list & out_list)) # 출력
