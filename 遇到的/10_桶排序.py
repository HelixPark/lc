# -*- coding:utf-8 -*-

def bucketSort(nums):
    maxValue, minValue = max(nums), min(nums)
    # 建立桶（个数）:每一个索引就是nums的数，存放的值是nums中出现的次数
    buckets = [0] * (maxValue - minValue + 1)

    # 维护桶
    for i in range(len(nums)):
        buckets[nums[i]-minValue] += 1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+minValue] * buckets[i]
    print(res)

nums = [5,3,6,1,2,7,5,10]
# 值都在1-10之间，建立10个桶：
bucketSort(nums)