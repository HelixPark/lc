from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 路径，选择列表
        def backtrack(first = 0, curr = []):
            # 组合完成，符合条件
            if len(curr) == k:
                return res.append(curr[:])
            # 选择列表
            for i in range(first, n):
                # 做选择
                curr.append(nums[i])
                # 回溯
                backtrack(i+1, curr)
                # 撤销选择
                curr.pop()


        res, n = [], len(nums)
        for k in range(n+1):
            backtrack()
        return res

c = Solution()
nums = [1,2,3]
c.subsets(nums)