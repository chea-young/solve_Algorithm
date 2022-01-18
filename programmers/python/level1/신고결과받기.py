def solution(id_list, report, k):
    report_num = [0 for i in range(len(id_list))]
    report_list = [[] for i in range(len(id_list))]
    for ele in report:
        ele = ele.split()
        index = id_list.index(ele[1])
        if ele[0] not in report_list[index]:
            report_list[index].append(ele[0])
            report_num[index] += 1
    answer = [0 for i in range(len(id_list))]
    user_num = []
    for index in range(len(report_num)):
        report_num[index] = report_num[index] // k
        if report_num[index] > 0:
            user_num.append(index)
    
    for num in user_num:
        for user in report_list[num]:
            index = id_list.index(user)
            answer[index] += 1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) #2 1 1 0
