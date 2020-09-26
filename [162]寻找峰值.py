# 峰值元素是指其值大于左右相邻值的元素。 
# 
#  给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。 
# 
#  数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。 
# 
#  你可以假设 nums[-1] = nums[n] = -∞。 
# 
#  示例 1: 
# 
#  输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。 
# 
#  示例 2: 
# 
#  输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5 
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
#  
# 
#  说明: 
# 
#  你的解法应该是 O(logN) 时间复杂度的。 
#  Related Topics 数组 二分查找 
#  👍 297 👎 0


class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        # 方式1：线性扫描、
        # 利用了连续的两个元素nums[j]和nums[j + 1]不会相等wei前提
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1
    def findPeakElement(self, nums: List[int]) -> int:
        # 方式2：迭代2分查找
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

    def findPeakElement3(self, nums: List[int]) -> int:
        # 方式3：递归二分查找
        # 利用：nums数组中的任何给定序列视为交替的升序和降序序列
        def find(nums,left,right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return find(nums,1,mid)
            return find(nums, mid+1, right)
        return find(nums,0,len(nums)-1)