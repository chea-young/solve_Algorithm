from itertools import combinations

def solution(orders, course):
    answer = []
    menu = []
    order_people = []

    for num in range(len(orders)):
        for alpha in orders[num]:
            if(alpha not in menu):
                menu.append(alpha)
                order_people.append([num])
            else:
                i = menu.indexof(alpha)
                l = order_people[i]
                l.append(num)
                order_people[i] = l
    
    for num in course:
        type = list(map(''.join, combinations(menu, num)))
        check = []
        for type_item in type:
            # 각 리스트 찾기
            alpha_list = []
            for c in type_item:
                i = menu.indexof(c)
                check.append(order_people[i])
            # 교집합하기
            first = alpha_list[0]
            for c in range(1,len(alpha_list)):
                first = first.intersection(alpha_list[c])
                if(len(first)==1):
                    break
            if(len(first)!=1):
                check.append((len(first), type_item))
        check = check.reverse()
        max_num  = check[0][0]
        answer.append(check[0][1])
        for i in range (1, len(check)):
            if(check[i][0] != max_num):
                break
            answer.append(check[i][1])
        return answer
    return answer