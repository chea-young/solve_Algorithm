def solution(m, musicinfos):
    info = []
    musicinfos_len = len(musicinfos)
    for i in range( musicinfos_len):
        information = musicinfos[i].split(',')
        # 악보 수정
        music_note = []
        music_count = 0
        while(music_count<len(information[-1])):
            note = information[-1][music_count]
            if(music_count+1!=len(information[-1]) and information[-1][music_count+1] =='#'):
                note+='#'
                music_count+=2
            else:
                music_count +=1
            music_note.append(note)
        # 시간 계산
        hour = int(information[1][0:2])-int(information[0][0:2])
        minute = int(information[1][3:])-int(information[0][3:])
        information[0] = hour*60+minute
        re = information[0]//len(music_note)
        if(information[0]%len(music_note)!=0):
            re +=1
        info.append([information[0], (music_note * re)[:information[0]],i, information[2]])
    m_note = []
    m_count = 0
    while(m_count < len(m)):
        note = m[m_count]
        if(m_count+1 != len(m) and m[m_count+1] =='#'):
            note+='#'
            m_count +=2
        else:
            m_count+=1
        m_note.append(note)
        answer = []
    for i in range(len(info)):
        num = info[i][1].count(m_note[0])
        if(num == 0):
            continue
        index = info[i][1].index(m_note[0])
        count = 0
        while(count < len(m_note) and index+count<len(info[i][1])):
            if(m_note[count] == info[i][1][index+count]):
                count+=1
            else:
                count = 0
                num-=1
                if(num==0):
                    break
                index = info[i][1].index(m_note[0],index+1,len(info[i][1]))
        if(num!=0 and count == len(m_note)):
            answer.append([(-1)*info[i][0],i,info[i][-1]])
    if(len(answer) == 0):
        return "(None)"
    answer.sort()
    return answer[0][2]

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"] ))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"] ))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"] ))