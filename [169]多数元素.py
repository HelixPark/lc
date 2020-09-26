# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。 
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [3,2,3]
# 输出: 3 
# 
#  示例 2: 
# 
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#  
#  Related Topics 位运算 数组 分治算法 
#  👍 724 👎 0


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
            if res == num:
                count += 1
            else:
                count -= 1
        return res