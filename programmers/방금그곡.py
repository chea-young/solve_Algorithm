def solution(m, musicinfos):
    info = []
    musicinfos_len = len(musicinfos)
    for i in range( musicinfos_len):
        info.append(musicinfos[i].split(','))
    answer = []
    for i in range(len(info)):
        print("in1")
        item = info[i][3]
        count = item.count(m[0])
        pre_index = item.index(m[0])
        for c in range(count):
            print("in2")
            index = pre_index
            if(c !=0):
                index = item.index(m[0], pre_index+1,len(item)-1)
            pre_index = index
            check = True
            for j in range(len(m)):
                if(index+j == len(item)):
                    index -= len(item)
                print(item,"in", item[index+j], m[j])
                if(item[index+j] != m[j]):
                    check = False
                    break
                sh = [0,0]
                try:
                    mus_note = item[index+j+1]
                except IndexError:
                    sh[0] = -1
                try:
                    m_note = m[j+1]
                except IndexError:
                    sh[1] = -1
                if(sh[0]== -1 or sh[1] == -1):
                    break
                else:
                    if(mus_note =='#' or m_note == '#'):
                        if(mus_note != m_note):
                            break
            print("out1")
            if(check):
                print("in3")
                hour = int(info[i][1][0:2])-int(info[i][0][0:2])
                minute = int(info[i][1][3:])-int(info[i][0][3:])
                answer.append([hour*(-1),minute*(-1),i,info[i][2]])
                break
    answer.sort()
    print(answer)
    if(len(answer) ==0):
        return "(None)"
    else:
        return answer[0][3]
            


print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"] ))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"] ))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"] ))