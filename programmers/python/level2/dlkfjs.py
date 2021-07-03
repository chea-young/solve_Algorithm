import heapq

def dijkstra(country, startPoint):
    # 최적화된 도로망이라는 country_opt_road 배열을 선언과 동시에 inf로 비어있는 상태로 
	# 선언해준다. input 되는 country에 있는 노드를 찾아서 포인트별로 저장하고 
	# 그 안의 값들은 일단 inf로 초기화 하는 작업의 코드 
    country_opt_road = {node: float('inf') for node in country} 
	# 최초 출발점은 input되는 startPoint로 설정하여 0으로 설정한다. 
	country_opt_road[startPoint] = 0 
	# 잠시 데이터를 쌓아둘 공간을 설정한다. 이 공간은 
	heap = [] 
	# heap공간에 Startpoint지점의 정보와 거리 0을 넣어준다. 
	heapq.heappush(heap, [country_opt_road[startPoint], startPoint]) 
	# heap 
    while heap : 
        distance , position = heapq.heappop(heap) 
        if country_opt_road[position] < distance : 
            continue 
        # input되는 country 데이터 안의 position이 가지는 초기값의 안의 정보를 
        # 가져온다. 그리고 안의 정보를 arrival , distance2로 나눠서 구분한다. 
        # B, 8이 나오고 기존의 inf를 바꿔주는 방식을 진행한다. 
        # 다음 arrival, distance2도 같은 작업을 해주고 
        # 끝이나면, 다음 노드로 넘어가서 그 노드의 items()를 가져와서 
        # 같은 작업을 반복 
        for arrival, distance2 in country[position].items() : 
            opt_distance = distance + distance2 
		    # 이부분을 통해 이전의 거리 계산 된 것과 비교하여 지금의 거리 값이 
            # 더 효율적이면 바꿔주는 코드이다. 
		    if opt_distance < country_opt_road[arrival] : 
			    print('최적화 작업 발생', arrival,'포인트에서 발생') 
                country_opt_road[arrival] = opt_distance 
                heapq.heappush(heap, [opt_distance, arrival]) 
                print(arrival ,country_opt_road) 
    return country_opt_road

