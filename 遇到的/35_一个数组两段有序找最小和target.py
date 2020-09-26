# -*- coding:utf-8 -*-
# 一个数组两段有序，找最小
class Solution:
    # 无重复情况：LC153
    def findMin1(self, nums: List[int]) -> int:
            left, right = 0, len(nums)-1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[right]:   #最小值在右边，往右边走
                    left = mid + 1
                elif nums[mid] < nums[right]:   #最小值在左边，往左边走
                    right = mid
            return nums[left]

    # 有重复情况：LC154和offer11
    def findMin2(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:   #最小值在右边
                left = mid + 1
            elif nums[mid] < nums[right]:  #最小值在左边
                right = mid
            else:
                # 相等时，有重复，直接right-1
                right -= 1
        return nums[left]

# 一个数组两段有序，找target
# 无重复的情况LC33
def fun(nums,left,right,target):
    while left <= right:
        mid = left + (right - left) // 2
        if target == nums[mid]:
            return mid
        # 中值小于右值，说明旋转点在mid的左边
        if nums[mid] <= nums[right]:
            # 都是先比较纯升序那段：target比中值大且比right小，则往右边走，否则左走
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        # 中值大于left，说明旋转点在mid后面
        elif nums[mid] >= nums[left]:
            # 都是先比较纯升序那段，target小于mid且大于left，往左边走，否则右边（含旋转点）走
            if target < nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # 找不到target
            return -1
    return -1
# 一个数组两段有序，找target
# 有重复的情况，面试题10.03
def search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        # 右边升序
        if arr[mid] < arr[left]:
            # 都是先比较纯升序那段：target比中值大且比right小，则往右边走，否则左走
            if target >= arr[left] or target <= arr[mid]:
                right = mid
            else:
                left = mid + 1
        # 中值大于left，说明旋转点在mid后面，左边升序
        elif arr[mid] > arr[left]:
            # 都是先比较纯升序那段，target小于mid且大于left，往左边走，否则右边（含旋转点）走
            if target <= arr[mid] and target >= arr[left]:
                right = mid
            else:
                left = mid + 1
        elif arr[left] == arr[mid]:
            # 如果左值等于中值，可能是已经找到了目标，也可能是遇到了重复值
            if arr[left] != target:
                left += 1  # 重复值
            else:
                right = left  # 找到了，

    if arr[left] == target:
        return left
    else:
        return -1

# nums = [4,5,6,7,0,1,2]
# nums = [1,1,1,1,1,2,1,1,1]
# print(fun(nums,0,len(nums)-1,2))
# nums = [4,5,6,7,0,1,2]
nums = [3,1]
print(fun(nums,0,len(nums)-1,1))