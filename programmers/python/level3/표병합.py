def solution(commands):
    global location, change_value, pre_data
    location = {} # (r, c): value  
    pre_data = {} #(r, c): value
    change_value = {} # value: value
    
    answer = []
    for c in commands:
        command = c.split()
        
        main_command = command[0]
        if main_command == 'UPDATE':
            excute_update(command[1:])
        elif main_command == 'MERGE':
            excute_merge(command[1:])
        elif main_command == 'UNMERGE':
            excute_unmerge(command[1:])
        elif main_command == 'PRINT':
            answer.append(excute_print(command[1:]))
        answer
    return answer
        
def excute_update(command):
    global location, change_value
    
    if len(command) == 3: # (r, c) 위치의 셀을 선택
        r, c, value = command
        location[(r, c)] = value
    else: # v1 -> v2로 변경
        value1, value2 = command
        change_value[value1] = value2

def excute_merge(command):
    global location, pre_data
    r1, c1, r2, c2 = command
    if (location and (r1, c1) in location):
        if((r2, c2) in location.keys()):
            pre_data[(r2, c2)] = location[(r2, c2)]
        location[(r2, c2)] = location[(r1, c1)]

def excute_unmerge(command):
    global location, pre_data
    r, c = command
    if (location and (r, c) in location):
        if(not pre_data and (r, c) in pre_data):
            location[(r, c)] = pre_data[(r, c)]
            del(pre_data[(r, c)])
        else:
            del(location[(r, c)])

def excute_print(command):
    global location
    r, c = command
    if (location and (r, c) in location):
        return find_real_value(location[(r, c)])
    else:
        return "EMPTY"

def find_real_value(value):
    global pre_data
    if (pre_data and value in pre_data):
        find_real_value(pre_data[value])
    else:
        return value  

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", 
"UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", 
"MERGE 1 2 1 3", "MERGE 1 3 1 4", 
"UPDATE korean hansik", "UPDATE 1 3 group", 
"UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])) # ["EMPTY", "group"]
#print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))