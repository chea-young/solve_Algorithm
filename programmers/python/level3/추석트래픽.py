def solution(lines):
    times = []
    # 구간 계산
    for i in range(len(lines)):
        info = lines[i].split()
        time_array = info[1].split(':')
        time = (float(time_array[0])*60+float(time_array[1]))*60+float(time_array[2])
        pre_time = time-float(info[2][:-1])
        times.append((round(time-float(info[2][:-1])+0.001,3),time))
    # 배열 만들어서 넣기

    # 최대값 구하기

print(solution(["2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"]))
