def solution(lines):
    times = []
    # 구간 계산
    for i in range(len(lines)):
        info = lines[i].split()
        time_array = info[1].split(':')
        time = (float(time_array[0])*60+float(time_array[1]))*60+float(time_array[2])
        times.append((int(round(time-float(info[2][:-1]),3)*1000)+1,int(time*1000)+1000))
    times.sort()
    # 최대값 구하기
    time_in = []
    now = times[0][0]
    answer = 0
    count = 0
    while(True):
        if(times == [] and time_in == []):
            break
        """for t in times:
            if(now == t[0]):
                time_in.append(t[1])
                count+=1
                times.remove(t)"""
        if(times != [] and now == times[0][0]):
            time_in.append(times[0][1])
            count+=1
            times.remove(times[0])
        for t in time_in:
            if(now==t):
                count -=1
                time_in.remove(t)
        if(count>answer):
            answer = count
        now += 1
    return answer
        
print(solution(["2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"]))
