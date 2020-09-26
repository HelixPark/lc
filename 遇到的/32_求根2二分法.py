# -*- coding:utf-8 -*-

def fun(x,e):
    low, high = 0, x
    mid = (low+high)/2
    while abs(mid * mid - x) > e:
        if mid * mid > x:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2
    return mid
x, e = 2, 0.00001
print(fun(x,e))