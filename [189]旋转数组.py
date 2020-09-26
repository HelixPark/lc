# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#  
# 
#  示例 2: 
# 
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100] 
# 
#  说明: 
# 
#  
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
#  要求使用空间复杂度为 O(1) 的 原地 算法。 
#  
#  Related Topics 数组 
#  👍 637 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 先全部旋转，再旋转前k个，再旋转后面的剩余
        # 当旋转数组k次，k% n个尾部元素会被移动到头部，剩下的元素会被向后移动
        k %= len(nums)
        def reverse(nums, start, end):
            while start < end:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start += 1
                end -= 1
        reverse(nums,0,len(nums) - 1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums) -1)

nums = [-1]
k = 2
c = Solution()
c.rotate(nums, k)