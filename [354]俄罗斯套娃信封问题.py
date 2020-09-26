from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 先按照w升序,h降序
        envelopes.sort(key=lambda x:(x[0], -x[1]))

        # 在对h列进行lis（最长递增子序列):DP LC300
        def lis(nums):
            if len(nums) <= 1:
                return len(nums)
            # 子序列最短也包括自己，base为1
            dp = [1] * len(nums)

            for i in range(1,len(nums)):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return max(dp)
        # 抽取h列
        return lis([i[1] for i in envelopes])