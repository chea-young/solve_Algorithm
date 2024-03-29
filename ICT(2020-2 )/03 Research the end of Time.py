def reachTheEnd(grid, maxTime):
    # Write your code here
    path = {}
    path_dict = {}
    grid_size = len(grid[0])
    row = 0
    col = 0
    while(True):
        if col == grid_size:
            col = 0
            row += 1
        if(row == grid_size):
            break
        key = f'({row}, {col})'
        path_dict[key] = []
        item = {}
        # check 동, 서, 남, 북
        try: #동
            if(grid[row][col+1] == '.'):
                change = col+1
                if(change != grid_size and change != -1):
                    item[f'({row}, {change})'] = 1
        except IndexError:
            pass
        try: #서
            if(grid[row][col-1] == '.'):
                change = col-1
                if(change != grid_size and change != -1):
                    item[f'({row}, {change})'] = 1
        except IndexError:
            pass
        try: #남
            if(grid[row+1][col] == '.'):
                change = row+1
                if(change != grid_size and change != -1):
                    item[f'({change}, {col})'] = 1
        except IndexError:
            pass
        try: #북
            if(grid[row-1][col] == '.'):
                change = row-1
                if(change != grid_size and change != -1):
                    item[f'({change}, {col})'] = 1
        except IndexError:
            pass
        path[key] = item
        col +=1
    if dijkstra(path, path_dict, grid_size)+1 == maxTime:
        return 'Yes'
    else:
        return 'No'

        
import heapq
def dijkstra(graph, path_dict,grid_size):
    start = '(0, 0)'
    distances = {node: float('inf') for node in graph}  
    distances[start] = 0  
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)  

        if distances[current_destination] < current_distance: 
            continue
    
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  
            if distance < distances[new_destination]:  
                    distances[new_destination] = distance
                    path_dict[new_destination] = path_dict[current_destination] + [current_destination]
                    heapq.heappush(queue, [distance, new_destination])
    size = grid_size-1
    return len(path_dict[f'({size}, {size})'])

print(reachTheEnd(['........#....#..#..#....#...#..#.#.#.#.#.#..#.....',
'..#..#..#.#....#..#.....#......#..##...........##.',
'.........#.###.##...#.....##......###............#',
'....##........#..#.#.#......#...#.##.......##.....',
'.................###...#.#...#......#.#.#.#.#...#.',
'.........#.....#...........##....#.#.#.##.....##..',
'.....#.##............#....#......#..#..#...##.....',
'.#.......###....#.#..##.##.#...##...#........#...#',
'..#.##..##..........#..........##.....##..........',
'#.#..##......#.#.#..##.###...#.........###..#...#.',
'.#..#..............#...#........#..#...#....#..#..',
'##..#..#........#....#........#...#.#......#.....#',
'#.#.......#.#..#...###..#..#.##...#.##.......#...#',
'#.#...#...#.....#....#......##.#.#.........#....#.',
'.#..........#......##..#....#....#.#.#..#..###....',
'#.#............#.##..#.##.##......###......#..#..#',
'.#..#.##...#.#......................#........#....',
'.....#....#.#..........##.#.#................#....',
'##............#.#......####...#.........#..##..#..',
'....#..##..##...#.........##..##....#..#.##...#...',
'.#........#...#..#...........#.###.....##.....##..',
'.......#..#..##...#..###.....#..##.........#......',
'...#......#..#...........###...............#......',
'...##.###.#.#....#...#..#.#.#....#....#.##.#...#..',
'..........#.......#..#..#...###....##.....#..#....',
'.............##.##.#.......#.#....#.......#..#..#.',
'.......#........#.....#....##...#...#.#...#.#.##..',
'.....#..#..#........#..#.....#...#.##.#....#...#..',
'....................#.#...#....###...###...##...#.',
'##.#.....##.....#..#.#.#...........#.#.##...#..#.#',
'#...........#....#.##...#.#.....#...#.....#.#.....',
'..#..##...#........#.##..#.....##.......#...#.#.#.',
'......#....#...##...........#..#.......#.##.......',
'......#..#..#.###..........#...#...........#..#...',
'....#.#..#..#.#.#...#.......#...#.##......#.......',
'....#.......#..#........#...#.#...#......#.......#',
'.#....##...#.#..#....#.#.##........#..#.#.........',
'#....#.......#..##......##...............#..#.##..',
'...#..##.......#.....#....#...#.#......#..##..###.',
'.....#...#...#...#...#...#..##...#..#.............',
'....##......#...#..#...#...#.#....#.....#..#.##...',
'...##.......#..##.....#........#.#....#...#.......',
'..#...#....#...#.###......#................#......',
'...#...###...#..##...###.....................#....',
'.....#....#....#...#.#.#.##....##......#....##....',
'...#.###...##.........#..........#.##.#.....#.....',
'##..#...#.........#.......#......##...........####',
'...###.#..........#.....#####........#..#.#.#...#.',
'...#..#.....#..##.##.#.....##...#...#.#.....#...##',
'.##.......#.##....#............#..................',
'#.....#.........#.#.........#..###....##...##.....',
'#....#.....#...#.....#.##...##...####........#....',
'#...........#..#...#........#.##..##..#...#.#.....',
'..#.#................#......###..##.#.#...##...#..',
'.#.#....#..#............#....#......#............#',
'..#..#...#.#.#...#...........#.......##.#...#.#...',
'#..........#.....#.....#......#.......#.#...##....',
'.......#...........#...........#....#............#',
'...####.#.....#.##.....#.......##.#..#......#.....',
'.#..#.....#..#......#.............#.#.#..##...#...',
'..#.#.#.........#...#..#.......#................##',
'.#..##.#.#...#.............#..#..........#..#...#.',
'....#........#......#...###..#.#..................',
'#..#..#.....#.#.#...##....##........#........#....',
'.....#.#.......##.......#.....#........#..##..#...',
'#.#.##........#..##.#..#.#...#........#.#......#..',
'....#.#.#.......#.##.##...##...#..#.###...#.#.#...',
'.....##.#....#........#....#.#........#.#.#.....#.',
'.....#..##..#.#....#.......#...#.#.###.........#.#',
'#.....#.##..#.......###.........#..##..#......##..'
], 2244))