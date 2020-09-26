# -*- coding:utf-8 -*-
# 可整合数组：如果一个数组在排序之后，每相邻两个数差的绝对值都为1，则该数组为可整合数组。
# 给定一个整型数组arr，请返回其中最大可整合子数组的长度。
# [5,3,4,6,2]排序之后为[2,3,4,5,6],符合每相邻两个数差的绝对值为1，
# 所以这个数组为可整合数组,返回5。若含重复，则肯定不是

def fun(nums):
    if not nums:
        return 0
    size, res = len(nums), 0

    for i in range(size):
        hashSet = set()
        maxValue, minValue = float('-inf'), float('inf')
        for j in range(i,size):
            if nums[j] in hashSet:
                break
            hashSet.add(nums[j])
            maxValue = max(maxValue, nums[j])
            minValue = min(minValue, nums[j])
            if maxValue - minValue == j - i:
                res = max(res, j -i +1)
    return res
nums = [5,3,4,6,2]
print(fun(nums))
