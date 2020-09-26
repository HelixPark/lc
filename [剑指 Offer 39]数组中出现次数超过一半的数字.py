# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。 
# 
#  
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2 
# 
#  
# 
#  限制： 
# 
#  1 <= 数组长度 <= 50000 
# 
#  
# 
#  注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/ 
# 
#  
#  Related Topics 位运算 分治算法 
#  👍 60 👎 0

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 可用hash方法、排序后取中点位置和摩尔投票法
        # 这里写摩尔投票:保存两个数组，一个计数，一个数字
        # 如果这个数字与之前保存的相同，次数+1，反之-1
        # 如果count为0，则保存下一个数字
        count, res = 0, 0
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        return res


nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
c = Solution()
print(c.majorityElement(nums))
