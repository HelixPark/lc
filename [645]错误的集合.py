# 集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重
# 复。 
# 
#  给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。 
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,2,2,4]
# 输出: [2,3]
#  
# 
#  注意: 
# 
#  
#  给定数组的长度范围是 [2, 10000]。 
#  给定的数组是无序的。 
#  
#  Related Topics 哈希表 数学 
#  👍 98 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def findErrorNums1(self, nums: List[int]) -> List[int]:
        # hash方式
        hashSet = set()
        res = []
        for i in nums:
            if i not in hashSet:
                hashSet.add(i)
            else:
                # 已出现，说明重复
                res.append(i)
        # 遍历找未出现的
        for i in range(1,len(nums)+1):
            if i not in hashSet:
                res.append(i)

        return res

    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 技巧方式
        n, dup = len(nums), -1
        # 元素从1开始的
        for i in range(n):

            index = abs(nums[i]) - 1

            if nums[index] < 0:
                dup = abs(nums[i])  # 找到了重复元素
            else:
                nums[index] *= -1

        miss = -1
        for i in range(n):
            if nums[i] > 0:
                # 找到了缺失的
                miss = i + 1
                break
        return [dup, miss]

# nums = [1,2,2,4]
nums = [3,3,1]
c = Solution()
c.findErrorNums(nums)