"""
원하는 것: 가장 많이 받은 친구가 받을 선물 수

[다음 달 +1 선물 기준]
+1: 두 사람 사이 더 많은 선물을 준 사람
+1: 기록이 X이거나 수가 같다면, 선물 지수가 큰 사람

[선물 지수]
- 이번 달까지 준 선물 - 받은 선물

[주고 받지 않는 경우]
- 선물 지수가 같으면 다음 달에 선물을 주고 받지 않음.


"""

from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    friend_gift_cnt = defaultdict(int) # 기록 산출
    gift_index = defaultdict(int) # 선물 지수
    
    # 1. 이번 달에 받은 선물, 선물 지수 계산하기
    for gift in gifts:
        friend_list = gift.split()
        give = friend_list[0]
        take = friend_list[1]
        
        friend_gift_cnt[gift] += 1
        gift_index[give] += 1
        gift_index[take] -= 1

    # 2. 다음 달에 추가로 받을 선물 계산하기
    next_month_gift = defaultdict(int)
    checked = set()
    
    for give in friends:
        for take in friends:
            
            forward_key = give + ' ' + take
            opposite_key = take + ' ' + give
            
            if (give == take):
                continue
            if forward_key in checked:
                continue
                
            forward = friend_gift_cnt[forward_key]
            opposite = friend_gift_cnt[opposite_key] if opposite_key in friend_gift_cnt.keys() else 0
        
            if (forward > opposite):
                next_month_gift[give] += 1
            elif (forward < opposite):
                next_month_gift[take] += 1
            else:
                if gift_index[give] > gift_index[take] :
                    next_month_gift[give] += 1
                elif gift_index[give] < gift_index[take] :
                    next_month_gift[take] += 1
        
            checked.update([forward_key, opposite_key])
    print(next_month_gift)
    print(next_month_gift.values())
    
    result_list = next_month_gift.values()
    return max(next_month_gift.values()) if result_list else 0
