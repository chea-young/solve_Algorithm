def solution(bridge_length, weight, truck_weights):
    time = 0
    now = []
    now_time = []
    while(True):
        time += 1
        if(sum(now) + truck_weights[0] <= weight):
            now.append(truck_weights.pop(0))
            now_time.append(1)
        if(truck_weights == []):
            return time + bridge_length
        for i in range(len(now_time)):
            now_time[i] += 1
        try:
            ind = now_time.index(bridge_length+1)
            del now[ind]
            del now_time[ind]
        except Exception:
            pass

        

print(solution(2, 10,[7,4,5,6]))
print(solution(100, 100,[10,10,10,10,10,10,10,10,10,10]))

def solution1(bridge_length, weight, truck_weights):
    time = 0
    now = {}
    while(True):
        time += 1
        if(sum(now) + truck_weights[0] < weight):
            now[truck_weights.pop(0)]=1
        key = list(now.keys())
        for k in key:
            now[k] = now[k]+1
            if(now[k]> bridge_length):
                del now[k]
        if(truck_weights == []):
            return time + bridge_length

