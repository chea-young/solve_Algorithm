#10816 숫자 카드2

# 입력
N = int(input())
dataN = map(int, input().split())
M = int(input())
dataM = map(int, input().split())

dataInfo = {}
for ele in dataN:
    if dataInfo and ele in dataInfo.keys():
        num = dataInfo[ele]
        dataInfo[ele] = num+1
    else:
        dataInfo[ele] = 1

answer = []
for ele in dataM:
    if ele in dataInfo.keys():
        answer.append(str(dataInfo[ele]))
    else:
        answer.append("0")

# 출력
print(" ".join(answer))
