def solution(info, query):
    answer = []
    A = ['java', 'cpp', 'python']
    B = ['backend', 'frontend']
    C = ['junior', 'senior']
    D = ['chicken', 'pizza']
    catalog = {}
    for information in info:
        temp = []
        person = information.split()
        temp.append(person[0])
        temp.append(person[1])
        temp.append(person[2])
        temp.append(person[3])
        temp = tuple(temp)
        if( temp in list(catalog.keys())):
            list_1 = catalog[temp]
            list_1.append(person[4])
            catalog[temp] = list_1
        else: 
            catalog[temp] = [person[4]]
    print(catalog)

    for q in query:
        temp = []
        ans = q.split()
        check = []
        if(ans[0] == '-'): temp.append(A)
        else: 
            temp.append(ans[0])
        if(ans[2] == '-'): temp.append(B)
        else: 
            temp.append(ans[2])
        if(ans[4] == '-'): temp.append(C)
        else: 
            temp.append(ans[4])
        if(ans[6] == '-'): temp.append(D)
        else: 
            temp.append(ans[6])
        num = 0
        """
        check_num = ans[7]
        if type(temp[0]) == list:
            for a in temp[0]:
                if type(temp[1]) == list:
                    for b in temp[1]:
                for c in temp[2]:
                    for d in temp[3]:
                        check_list = catalog[(a,b,c,d)]
                        for number in check_list:
                            if(number>check_num): num += 1
"""



    #return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])