# -*- coding:utf-8 -*-

def intervalSchedule(intvs):

    if len(intvs) == 0:
        return 0
    # 按区间的end升序拍嘞
    intvs.sort(key=lambda x : x[1])

    count = 1
    # 第一个区间就是end
    x_end = intvs[0][1]
    for i in intvs:
        start = i[0]
        if start >= x_end:
            # 找到下一个不重复区间了
            count += 1
            x_end = i[1]
    return count

intvs = [[1,3], [2,4], [3,6]]
print(intervalSchedule(intvs))