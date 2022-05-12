""" 
판매원 -> 파매의 10%를  추천인 배분/나머지 가집
추천인이 판매한 10%는 자기꺼

"""

# 현재 이익 계산하기
def update_benefit(name, cost):
    global benefit, conn
    give_cost = cost//10
    my_cost = cost - give_cost
    
    # 배분할 금액이 0보다 작은 경우
    if give_cost <= 0:
        benefit[name] += cost
    else:
        benefit[name] += my_cost
        next_name = conn[name]
        if next_name != '-': # 다음 추천인이 center가 아닌 경우
            update_benefit(next_name, give_cost)

def solution(enroll, referral, seller, amount):
    global benefit, conn
    answer = []

    # 추천인에 대한 dict 만들기
    conn = {e: '' for e in enroll}
    for i in range(len(enroll)):
        conn[enroll[i]] = referral[i]

    # 이익 확인하기
    benefit = {e: 0 for e in enroll}
    order_cnt = len(seller)
    for i in range(order_cnt):
        update_benefit(seller[i], amount[i]*100)
    
    # enroll 순서대로 list 구성하기
    for i in range(len(enroll)):
        answer.append(benefit[enroll[i]])
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))