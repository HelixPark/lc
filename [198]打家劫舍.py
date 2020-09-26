from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if l <= 2:
            return max(nums)
        # 转移方程：遇到第i个房屋，若抢i，则加上i-2的值，否则就是i-1的值
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        dp = [0] * l
        # base case
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2,l):

            dp[i] = max(dp[i-1],   #不抢第i个
                        dp[i-2] + nums[i])   #抢第i个

        return dp[l-1]

n = [1,2,3,1]
c = Solution()
print(c.rob(n))