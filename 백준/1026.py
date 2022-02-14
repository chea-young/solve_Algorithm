#보물
num = int(input())
# 입력
a_list = [int(i) for i in input().split()] 
b_list = [int(i) for i in input().split()] 
sort_a = sorted(a_list)
sort_b = sorted(b_list)
answer  = 0
for i in range(num):
    answer += sort_a[i] * sort_b[num-i-1]
print(answer) # 출력
