import math

# 요금 계산하는 함수
def cal_fee(total_mins):
    total_fee = 0
    if total_mins <= fee_data[0][0]: # 기본요금을 넘지 않은 경우
        total_fee = fee_data[0][1]
    else:
        plus_mins = total_mins-fee_data[0][0]
        plus_fee = math.ceil(plus_mins/fee_data[1][0])*fee_data[1][1]
        total_fee = fee_data[0][1]+plus_fee
    return total_fee

def solution(fees, records):
    global fee_data
    answer = [] # (차량번호, 요금)
    
    # 주차 요금 데이터 정리
    fee_data = [(fees[0], fees[1]), (fees[2], fees[3])]
    
    # 주차 시간
    in_car = {} # 차번호: 들어온시간
    out_car = {}
    for ele in records:
        data = ele.split()
        time = list(map(int, data[0].split(':')))
        
        if data[-1] == 'IN': # 입차인경우
            in_car[data[1]] = time
            
        elif data[-1] == 'OUT': # 출차인경우
            in_data = in_car[data[1]]
            total_time = [time[0]-in_data[0], time[1]-in_data[1]]
            total_mins = total_time[0]*60 + total_time[1]
            out_car[data[1]] = out_car.get(data[1], 0) + total_mins
            del(in_car[data[1]])
            
    # 출차 내역이 없는 차 시간 계산
    for car, time in in_car.items():
        total_time = [23-time[0], 59-time[1]]
        total_mins = total_time[0]*60 + total_time[1]
        
        out_car[car] = out_car.get(car, 0) + total_mins
        
    # 요금 계산
    for car, time in out_car.items():
        total_fee = cal_fee(time)
        answer.append((car, total_fee))
    
    # 차량번호가 작은 자동차순으로 주차요금 정렬
    answer.sort()
    answer = [i[-1] for i in answer]
    
    return answer
