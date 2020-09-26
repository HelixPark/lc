# -*- coding:utf-8 -*-
# 希尔排序是把记录按下标的一定增量分组，
# 对每组使用直接插入排序算法排序；
# 随着增量逐渐减少，每组包含的关键词越来越多，
# 当增量减至1时，整个文件恰被分成一组，算法便终止。

def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)
    # 升序
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)

arr = [12, 34, 54, 2, 3]

n = len(arr)
print(arr),
shellSort(arr)
print(arr),