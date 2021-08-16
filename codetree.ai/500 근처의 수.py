num = list(map(int, input().split()))

num_less_500 = 0
num_more_500 = max(num)

for element in num:
    if element < 500:
        num_less_500 = max(num_less_500, element)
    else:
        num_more_500 = min(num_more_500, element)

print(num_less_500, num_more_500)