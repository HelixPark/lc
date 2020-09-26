# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
# 
#  你可以假设数组中无重复元素。 
# 
#  示例 1: 
# 
#  输入: [1,3,5,6], 5
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [1,3,5,6], 2
# 输出: 1
#  
# 
#  示例 3: 
# 
#  输入: [1,3,5,6], 7
# 输出: 4
#  
# 
#  示例 4: 
# 
#  输入: [1,3,5,6], 0
# 输出: 0
#  
#  Related Topics 数组 二分查找 
#  👍 579 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# utf-8
from typing import List
class Solution:
    def searchInsert1(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums) and nums[i] < target:
            i += 1
        return i
    def searchInsert2(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:return i
        return len(nums)
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分查找
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left



nums = [1, 3, 5, 6]
target = 7
c = Solution()
print(c.searchInsert(nums, target))