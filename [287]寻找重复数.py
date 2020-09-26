# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出
# 这个重复的数。 
# 
#  示例 1: 
# 
#  输入: [1,3,4,2,2]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [3,1,3,4,2]
# 输出: 3
#  
# 
#  说明： 
# 
#  
#  不能更改原数组（假设数组是只读的）。 
#  只能使用额外的 O(1) 的空间。 
#  时间复杂度小于 O(n2) 。 
#  数组中只有一个重复的数字，但它可能不止重复出现一次。 
#  
#  Related Topics 数组 双指针 二分查找 
#  👍 856 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 调换的方式
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i] == nums[nums[i]-1]:
                    return nums[i]
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
                # 使用下面这一行，结果不对
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]

    def findDuplicate1(self, nums: List[int]) -> int:
        # 乘-1的方式
        for num in nums:
            num = abs(num)
            if nums[num-1] > 0:
                nums[num-1] *= -1
            else:
                return num
c = Solution()
c.findDuplicate1([1,3,4,2,2,])