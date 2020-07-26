import math

def solution(w,h):
    if(w == h):
        return w*h-w
    short_l,long_l = h,w
    if(h>w):
        short_l,long_l = w,h
    pre_value = long_l
    all = w*h
    for i in range(1,short_l+1):
        value = (-1)*long_l*i/short_l+long_l
        all -= math.ceil(pre_value-value)
        pre_value = value
    return all

print(solution(8,12))