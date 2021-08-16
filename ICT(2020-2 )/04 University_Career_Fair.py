def maxEvents(arrival, duration):
    info = {}
    num = len(arrival)
    for i in range(num):
        item = 0
        try:
            if(info[arrival[i]]> duration[i]):
                info[arrival[i]] = duration[i]
        except:
            info[arrival[i]] = duration[i]
            
    arrival = sorted(list(info.keys()))
    dur_time = [i +info[i] for i in arrival]
    event = 0
    time = 0
    while(True):
        item = find_next(arrival, dur_time, time)
        if(item ==None):
            break
        arrival = item[0]
        dur_time = item[1]
        time = item[2]
        event +=1
    return event

import numpy as np
def find_next(arrival, dur_time, nowtime):
    del_index = [i for i in range(len(arrival)) if nowtime > arrival[i]]
    np_arri = np.array(arrival)
    np_dur_time = np.array(dur_time)

    np_arri = np.delete(np_arri, del_index)
    np_dur_time = np.delete(np_dur_time, del_index)
    if(list(np_arri) == []):
        return None
    min_dur = np.min(np_dur_time)
    index = np.where((np_dur_time==min_dur))[0][0]
    arri = np.delete(np_arri, index)
    dur_time = np.delete(np_dur_time, index)
    return((list(arri), list(dur_time), min_dur))

print(maxEvents([1,3,5], [2,2,2]))