from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] == nums[i]:
                    count += 1
        return count