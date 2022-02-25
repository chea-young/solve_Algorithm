#색칠하기 13265

#입력
case = int(input())
data = []
for c in range(case):
    circle, line = map(int, input().split())
    ele = []
    for l in range(line):
        x, y = map(int, input().split())
        ele.append((x, y))
    data.append(ele)

for case_data in data:
    checked_circle = [0 for i in range(len(case_data)+1)]
    state = True
    for ele in case_data:
        if checked_circle[ele[0]] == checked_circle[ele[1]] == 0:
            checked_circle[ele[0]] = 1
            checked_circle[ele[1]] = -1
        elif checked_circle[ele[0]] == checked_circle[ele[1]]: # impossible 경우, 선으로 이어져 있는데 같은 색이 칠해져 있을 때
            state = False
            break
        elif checked_circle[ele[0]] != 0:
            checked_circle[ele[1]] = (-1) * checked_circle[ele[0]]
        elif checked_circle[ele[1]] != 0:
            checked_circle[ele[0]] = (-1) * checked_circle[ele[1]]
    # 출력
    if state: print("possible") 
    else: print("impossible")
