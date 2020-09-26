from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        # i为索引，存为values，n存为key值
        for i, n in enumerate(nums):
            if target - n in dict:
                return [dict[target - n], i]
            dict[n] = i

nums = [2, 11, 11, 7]
target = 9

c = Solution()
c.twoSum(nums,target)